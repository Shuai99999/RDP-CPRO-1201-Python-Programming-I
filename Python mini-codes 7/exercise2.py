def get_class_scores(class_number):
    scores_input = input(f"Enter scores for class {class_number} separated by spaces: ")
    parts = scores_input.strip().split()
    scores = []
    for item in parts:
        scores.append(float(item))
    return scores


def calculate_average(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    if count == 0:
        return 0
    return total / count


def weighted_average():
    n = int(input("How many classes? "))

    class_averages = []
    class_sizes = []

    i = 0
    while i < n:
        scores = get_class_scores(i + 1)

        total = 0
        count = 0
        for s in scores:
            total += s
            count += 1

        avg = total / count if count != 0 else 0
        class_averages.append(avg)
        class_sizes.append(count)

        print(f"Average for class {i + 1}: {avg:.2f}")
        i += 1

    total_weighted_score = 0
    total_students = 0
    j = 0
    while j < n:
        total_weighted_score += class_averages[j] * class_sizes[j]
        total_students += class_sizes[j]
        j += 1

    department_avg = total_weighted_score / total_students if total_students != 0 else 0
    print(f"\nDepartment weighted average: {department_avg:.2f}")


weighted_average()
