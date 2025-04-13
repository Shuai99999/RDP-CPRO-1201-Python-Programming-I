def solve_torque_system():
    print("=== Rotational Equilibrium Solver ===")
    print("Enter each force and its distance from the pivot.")
    print("If force or distance is unknown, enter 'x'")
    print("Enter 'done' to finish input.\n")

    equations = []
    unknowns = []

    while True:
        entry = input(
            "Enter force and distance (e.g. 10 3), or 'x 4', or 'done': "
        ).strip()
        if entry.lower() == "done":
            break
        parts = entry.split()
        if len(parts) != 2:
            print("Invalid input. Enter two values.")
            continue

        force, distance = parts
        if force == "x" and distance == "x":
            print("At least one value must be known.")
            continue

        if force == "x":
            var = f"F{len(unknowns)+1}"
            unknowns.append(var)
            try:
                d = float(distance)
                equations.append((var, d))
            except:
                print("Invalid distance.")
        elif distance == "x":
            var = f"D{len(unknowns)+1}"
            unknowns.append(var)
            try:
                f = float(force)
                equations.append((f, var))
            except:
                print("Invalid force.")
        else:
            try:
                f = float(force)
                d = float(distance)
                equations.append((f * d))
            except:
                print("Invalid number input.")

    if not unknowns:
        total = sum(equations)
        if abs(total) < 1e-6:
            print("\nThe system is in rotational equilibrium.")
        else:
            print("\nThe system is NOT in rotational equilibrium.")
    elif len(unknowns) == 1:
        known_total = 0
        for item in equations:
            if isinstance(item, (int, float)):
                known_total += item
            elif isinstance(item[0], str):
                continue
            else:
                known_total += item[0] * item[1]

        var, coeff = next(
            (
                i
                for i in equations
                if isinstance(i, tuple) and i[0] in unknowns or i[1] in unknowns
            )
        )
        if isinstance(coeff, str):  # unknown is distance
            result = -known_total / var
            print(f"\nSolution: {coeff} = {result}")
        else:  # unknown is force
            result = -known_total / coeff
            print(f"\nSolution: {var} = {result}")
    else:
        print("\nThe system has multiple unknowns.")
        print("This version only solves problems with one unknown.")
        print("Result: Infinite or no solutions depending on values.")


solve_torque_system()
