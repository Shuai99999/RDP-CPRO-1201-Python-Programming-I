user_input = input(
    "Please provide, displacement, initial velocity, and acceleration: "
).split(",")
displacement = int(user_input[0])
v = int(user_input[1])
acceleration = int(user_input[2])
# S=v t + ½ a t²
t = round((2 * displacement / acceleration) ** 0.5, 2)
print(f"Time of travel is {t} seconds.")
