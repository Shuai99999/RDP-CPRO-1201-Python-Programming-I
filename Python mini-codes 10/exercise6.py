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
        if i in r"[$#@%]":
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
