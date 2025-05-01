import re


def is_password_valid(password):
    # a)	The password is all small letters
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    # b)	The password is all capital letters
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    # c)	The password doesn’t have any digits
    if len(re.findall(r"\d", password)) < 1:
        return False, "Password must contain at least one digits."

    # d)	The password only has digits
    if len(re.findall(r"\d", password)) == len(password):
        return False, "Password only has digits."

    # e)	The password doesn’t contain any special characters (@#$%^&*~)
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 1:
        return False, "Password must contain at least one special characters."

    # f)	The password only contains special characters
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) == len(password):
        return False, "Password only has special characters."

    # g)	The password doesn't have repeating characters
    if len(password) == len(set(password)):
        return False, "Password doesn't have repeating characters."

    # h)	The password is not palindrome (symmetric)
    if password != password[::-1]:
        return False, "Password is not palindrome."

    # i)	The password is only palindrome (symmetric)
    if password == password[::-1]:
        return False, "Password is only palindrome."

    # Check if password is longer than 6 characters
    # if len(password) <= 6:
    #     return False, "Password must be longer than 6 characters."

    # If all checks pass
    return True, "Password is valid."


is_valid = False

while not is_valid:
    password = input("Enter your password: ")
    is_valid, message = is_password_valid(password)
    print(message)
