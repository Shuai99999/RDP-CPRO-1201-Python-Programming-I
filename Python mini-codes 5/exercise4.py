import re


def is_password_valid(password):
    # Check if password is longer than 6 characters
    if len(password) <= 6:
        return False, "Password must be longer than 6 characters."

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    # Check for at least two digits
    if len(re.findall(r"\d", password)) < 2:
        return False, "Password must contain at least two digits."

    # Check for at least two special characters
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 2:
        return False, "Password must contain at least two special characters."

    # If all checks pass
    return True, "Password is valid."


# Take password input from the user
password = input("Enter your password: ")

# Validate the password
is_valid, message = is_password_valid(password)
print(message)
