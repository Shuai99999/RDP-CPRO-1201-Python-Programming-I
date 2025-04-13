def atwood_solver():
    print("=== Atwood Pulley System Solver ===")
    try:
        m1 = float(input("Enter mass m1 (kg): "))
        m2 = float(input("Enter mass m2 (kg): "))
        m_rope = float(input("Enter rope mass (kg, enter 0 if negligible): "))
    except:
        print("Invalid input. Please enter numbers.")
        return

    g = 9.81

    if m1 == m2 and m_rope == 0:
        print("\nMasses are equal and rope is massless. System is in equilibrium.")
        print("Acceleration: 0 m/s²")
        print("Tension: {:.2f} N".format(m1 * g))
        return

    total_mass = m1 + m2 + m_rope
    net_force = (m2 - m1) * g

    a = net_force / total_mass

    # Tension on m1 side (approximate if rope has mass)
    T1 = m1 * (g + a)
    # Tension on m2 side (optional)
    T2 = m2 * (g - a)

    print("\nResult:")
    print("Acceleration of the system: {:.3f} m/s²".format(a))
    print("Tension near m1: {:.3f} N".format(T1))
    print("Tension near m2: {:.3f} N".format(T2))


atwood_solver()
