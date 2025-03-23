def get_student_grade(students):
    student_dict = {name: grade for name, grade in students}
    student_name = input("Enter the student's name: ")

    if student_name in student_dict:
        print(f"{student_name}'s grade: {student_dict[student_name]}")
    else:
        print("Student not found.")


students = [("Ethan", 90), ("Olivia", 85), ("Mason", 92), ("Jack", 88)]
get_student_grade(students)
