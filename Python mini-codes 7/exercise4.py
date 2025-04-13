import time


def check_password(target):
    charset = "abcdefghijklmnopqrstuvwxyz0123456789"
    found = ""
    total_loops = 0

    for target_char in target:
        for c in charset:
            total_loops += 1
            if c == target_char:
                found += c
                break

    return total_loops


def password_checker():
    password = input("Enter a password (lowercase letters and digits only): ")
    start_time = time.time()
    tries = check_password(password)
    elapsed = time.time() - start_time

    print(f"Password found in {tries} tries.")
    print(f"Time taken: {elapsed:.4f} seconds")


password_checker()
