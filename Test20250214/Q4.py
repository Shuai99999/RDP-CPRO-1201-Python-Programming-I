list_num = int(input('Please input the list number you want: '))
user_list = []
for i in range(list_num):
    list_mem = int(input('Please input list numbers: '))
    user_list.append(list_mem)

for i in range(len(user_list)):
    for j in range(i + 1, len(user_list)):
        if user_list[i]<user_list[j]:
            user_list[i], user_list[j] = user_list[j], user_list[i]
print(user_list)