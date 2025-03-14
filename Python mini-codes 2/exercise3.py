import math


def calculate_time(displacement, velocity, acceleration):
    if acceleration == 0:  # Avoid division by zero
        if velocity == 0:
            return "Time cannot be determined (no motion)."
        return f"Time of travel is {displacement / velocity:.2f} seconds"

    # Solving quadratic equation: at² + 2vt - 2s = 0
    a = 0.5 * acceleration
    b = velocity
    c = -displacement

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return "No real solution (motion not possible with given values)."

    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # Return the valid (non-negative) time
    times = [t for t in [t1, t2] if t >= 0]
    if times:
        return f"Time of travel is {min(times):.2f} seconds"
    return "No valid positive time solution."


# Taking user input
s = float(input("Enter displacement (m): "))
v0 = float(input("Enter initial velocity (m/s): "))
a = float(input("Enter acceleration (m/s²): "))

# Output the result
print(calculate_time(s, v0, a))
