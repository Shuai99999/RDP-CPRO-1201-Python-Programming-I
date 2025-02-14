list_num = int(input("How many number: "))
user_list = []
for i in range(list_num):
    list_member = int(input("Please input a number: "))
    user_list.append(list_member)

list_sum = 0
for i in user_list:
    list_sum += i
avg = list_sum / list_num

standard_deviation = 0
standard_deviation_divide = 0
for i in user_list:
    standard_deviation += (i - avg) ** 2
    if (i - avg) != 0:
        standard_deviation_divide += 1
standard_deviation = (standard_deviation / standard_deviation_divide) ** 0.5
print(avg)
print(standard_deviation)
