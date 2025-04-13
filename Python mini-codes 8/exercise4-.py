def solve_kinematics():
    print("=== Kinematics Solver with Friction ===")
    try:
        M = float(input("Enter the mass of the object (kg): "))
        mu_s = float(input("Enter static friction coefficient (μs): "))
        mu_k = float(input("Enter kinetic friction coefficient (μk): "))
        F = float(input("Enter the applied horizontal force (N): "))
    except:
        print("Invalid input. Please enter numbers.")
        return

    g = 9.81  # 重力加速度 m/s^2
    N = M * g  # 正常力
    f_s_max = mu_s * N  # 最大静摩擦力

    print("\nCalculating...")

    if F <= f_s_max:
        print("The object will NOT move.")
        print(
            f"Reason: Applied force ({F:.2f} N) ≤ max static friction ({f_s_max:.2f} N)"
        )
    else:
        f_k = mu_k * N  # 动摩擦力
        a = (F - f_k) / M
        print("The object WILL move.")
        print(f"Acceleration: {a:.2f} m/s²")


solve_kinematics()
