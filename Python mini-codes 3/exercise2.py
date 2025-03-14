def check_elastic_collision(m1, v1i, m2, v1f):
    # Step 1: Calculate the velocity of the second object after collision using momentum conservation
    if m2 == 0:  # Prevent division by zero
        return "Invalid input: Mass of the second object cannot be zero."

    v2f = (m1 * v1i - m1 * v1f) / m2  # Derived from momentum conservation

    # Step 2: Calculate initial and final kinetic energies
    KE_initial = 0.5 * m1 * v1i**2
    KE_final = 0.5 * m1 * v1f**2 + 0.5 * m2 * v2f**2

    # Step 3: Check if the collision is elastic
    if abs(KE_initial - KE_final) < 1e-6:  # Allowing small floating-point errors
        return f"The collision is ELASTIC. Final velocity of the second object: {v2f:.2f} m/s"
    else:
        return f"The collision is INELASTIC. Final velocity of the second object: {v2f:.2f} m/s"


# Taking user input
m1 = float(input("Enter mass of first object (kg): "))
v1i = float(input("Enter initial velocity of first object (m/s): "))
m2 = float(input("Enter mass of second object (kg): "))
v1f = float(input("Enter final velocity of first object (m/s): "))

# Output the result
print(check_elastic_collision(m1, v1i, m2, v1f))
