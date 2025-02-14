list_num = int(input("How many number: "))
num_list = []
for i in range(list_num):
    list_member = int(input("Please input a number: "))
    num_list.append(list_member)


for i in range(0, len(num_list)):
    for j in range(i + 1, len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)
