month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

num = int(input("Enter a month number (1-12): "))

if 1 <= num <= 12:
    print(f"The month is {month_dict[num]}")
else:
    print("Invalid month number!")

month_name = input("Enter a month name: ").strip().capitalize()

reverse_month_dict = {v: k for k, v in month_dict.items()}

if month_name in reverse_month_dict:
    print(f"The month number for {month_name} is {reverse_month_dict[month_name]}")
else:
    print("Invalid month name!")
