def parse_input(input_str):
    result = {}
    parts = input_str.strip("{}").split(", ")
    for part in parts:
        if ":" not in part:
            continue
        name, age = part.split(":")
        name = name.strip(" \"'")
        age = int(age.strip())
        result[name] = age
    return result


def sort_dict_by_age(d):
    items = list(d.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return dict(items)


input_str = input("Enter dictionary (format: {'Name': age, ...}): ")
user_dict = parse_input(input_str)
sorted_dict = sort_dict_by_age(user_dict)
print(sorted_dict)

# Input: {'Alice': 25, 'Bob': 20, 'Charlie': 30}
