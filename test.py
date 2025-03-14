# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)


# print(factorial(5))
# print(power(4, 4))


# Q6
# a)
# def GCD_recursively(x, y):
#     if y == 0:
#         return "The recursively function result is: " + str(x)
#     else:
#         # print(x, y)
#         return GCD_recursively(y, x % y)


# print(GCD_recursively(103488, 2568384))
# print(GCD_recursively(67327284, 76437628))


# # b)
# def GCD_loop(x, y):
#     while y != 0:
#         x, y = y, x % y
#         # print(x, y)
#     return "The loop function result is: " + str(x)


# print(GCD_loop(103488, 2568384))
# print(GCD_loop(67327284, 76437628))

# 6 小写 大写 special 数字2个


def is_password_valid(password):
    # Check if password is longer than 6 characters
    if len(password) < 6:
        return False, "Password must not be less than 6 characters."

    # Check for at least one uppercase letter
    upper_counter = 0
    for i in password:
        if "A" <= i <= "Z":
            upper_counter += 1
    if upper_counter < 1:
        return False, "Password must contain at least one uppercase letter."

    lower_counter = 0
    for i in password:
        if "a" <= i <= "z":
            lower_counter += 1
    if lower_counter < 1:
        return False, "Password must contain at least one lowercase letter."

    # Check for at least two digits
    digital_counter = 0
    for i in password:
        if "0" <= i <= "9":
            digital_counter += 1
    if digital_counter < 2:
        return False, "Password must contain at least two digits."

    # Check for at least one special character
    special_counter = 0
    for i in password:
        if i in r'[!@#$%^&*(),.?":{}|<>]':
            special_counter += 1
    if special_counter < 1:
        return False, "Password must contain at least one special character."

    # If all checks pass
    return True, "Password is valid."


# Take password input from the user
password = input("Enter your password: ")

# Validate the password
is_valid, message = is_password_valid(password)
print(message)
