import random
import string


def generate_password(length=10):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    specials = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    all_chars = uppercase + lowercase + digits + specials

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(specials),
    ]

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return "".join(password)


def password_generator():
    while True:
        pwd = generate_password()
        print("Generated password:", pwd)
        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


password_generator()
