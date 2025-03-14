# user_email = input("Please input your email: ")
user_email = "John.travolta@rdpolytech.ca"

first_name = user_email.split(".", 1)[0]
last_name = user_email.split(".", 1)[1].split("@", 1)[0]
print(first_name)
print(last_name)
