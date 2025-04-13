from datetime import datetime, timedelta

year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))

current_date = datetime(year, month, day)

next_day = current_date + timedelta(days=1)

print("The next date is", next_day.strftime("%Y-%m-%d"))
