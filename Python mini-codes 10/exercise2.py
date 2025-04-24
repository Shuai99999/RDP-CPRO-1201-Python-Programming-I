month = input("Input the month (e.g. January, February etc.): ").strip().capitalize()
day = int(input("Input the day: "))

if (
    (month == "December" and day >= 21)
    or (month in ["January", "February"])
    or (month == "March" and day < 20)
):
    season = "Winter"
elif (
    (month == "March" and day >= 20)
    or (month in ["April", "May"])
    or (month == "June" and day < 21)
):
    season = "Spring"
elif (
    (month == "June" and day >= 21)
    or (month in ["July", "August"])
    or (month == "September" and day < 22)
):
    season = "Summer"
elif (
    (month == "September" and day >= 22)
    or (month in ["October", "November"])
    or (month == "December" and day < 21)
):
    season = "Fall"
else:
    season = "Unknown"

# Output the result
print("Season is", season)
