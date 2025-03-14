grade = int(input("Enter the student's grade (0-100): "))

if 95 <= grade <= 100:
    letter_grade = "A+"
elif 90 <= grade < 95:
    letter_grade = "A"
elif 85 <= grade < 90:
    letter_grade = "A-"
elif 80 <= grade < 85:
    letter_grade = "B+"
elif 75 <= grade < 80:
    letter_grade = "B"
elif 70 <= grade < 75:
    letter_grade = "B-"
elif 65 <= grade < 70:
    letter_grade = "C+"
elif 0 <= grade < 65:
    letter_grade = "F"
else:
    letter_grade = "Invalid grade"

print(f"The letter grade is: {letter_grade}")
