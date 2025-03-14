def mechanical_energy(mass, velocity, height):
    g = 9.81  # Acceleration due to gravity (m/s²)
    KE = 0.5 * mass * velocity**2  # Kinetic Energy
    PE = mass * g * height  # Potential Energy
    ME = KE + PE  # Mechanical Energy
    return f"The mechanical energy is {ME:.2f} Joules"


# Taking user input
mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
height = float(input("Enter height (m): "))

# Output the result
print(mechanical_energy(mass, velocity, height))
