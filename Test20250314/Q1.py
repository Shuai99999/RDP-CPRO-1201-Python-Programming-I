list_num = int(input("How many number would you like to create: "))
user_list = []
for i in range(list_num):
    list_member = int(input("Please input a number: "))
    user_list.append(list_member)

print([i**3 for i in user_list if i % 2 == 1])
