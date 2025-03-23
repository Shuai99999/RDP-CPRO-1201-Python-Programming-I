def find_max_key(d):
    max_key = None
    max_value = list(my_dict.values())[0]

    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key


my_dict = {"a": 10, "b": 20, "c": 15}
print(find_max_key(my_dict))
