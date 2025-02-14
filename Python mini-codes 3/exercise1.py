user_phone_number = input("What is your phone number: ")

is_Alberta = user_phone_number[:3] in ["403", "780", "587"]
print(f"It is {is_Alberta} that the email is from Alberta.")
