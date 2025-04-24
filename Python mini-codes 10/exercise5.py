month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

month = input("Input the name of Month: ").strip().capitalize()

if month in month_days:
    print(f"Number of days in {month}: {month_days[month]}")
else:
    print("Invalid month name.")
