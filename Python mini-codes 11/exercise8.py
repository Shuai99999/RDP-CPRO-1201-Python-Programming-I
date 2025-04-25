stu_grades = {
    "Sina": 10,
    "Amir": 20,
    "Elham": 17,
    "Mahtab": 9,
    "Hossein": 20,
    "Fateme": 15.75,
    "Elnaz": 16.2,
    "Ahmad": 18.5,
}

help_list = [name.upper() for name, grade in stu_grades.items() if grade < 16]

print(help_list)
