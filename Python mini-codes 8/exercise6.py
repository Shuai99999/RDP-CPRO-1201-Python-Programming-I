def pulley_horizontal_vertical():
    print("=== Pulley System (One on Table, One Hanging) ===")
    try:
        m1 = float(input("Enter mass on the table (m1 in kg): "))
        m2 = float(input("Enter hanging mass (m2 in kg): "))
    except:
        print("Invalid input. Please enter valid numbers.")
        return

    g = 9.81  # gravity

    a = (m2 * g) / (m1 + m2)
    T = m1 * a

    print("\nResults:")
    print(f"Acceleration of the system: {a:.3f} m/s²")
    print(f"Tension in the rope: {T:.3f} N")


pulley_horizontal_vertical()
