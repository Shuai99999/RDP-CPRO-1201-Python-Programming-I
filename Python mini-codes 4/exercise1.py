user_number = input("Please input your phone number: ")
# print(user_number[0:3])
if user_number[0:3] in ["403", "780", "587"]:
    print("You phone number is from Alberta.")
else:
    print("You phone number is not from Alberta.")
