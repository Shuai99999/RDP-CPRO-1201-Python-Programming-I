def student_grade(*scores, student_name="Myla"):
    avg = sum(scores) / len(scores)
    return f"{student_name} gets an average score of {round(avg, 1)}"


print(student_grade(20, 16, 17, 19, student_name="Chloe"))
