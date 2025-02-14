user_input = input("What is your first name, last name, and RDP email address: ").split(
    ","
)
first_name = user_input[0]
last_name = user_input[1]
input_email = user_input[2]
email = first_name + "." + last_name + "@rdpolytech.ca"
print(f"It is {email == input_email} that the email is correct.")
