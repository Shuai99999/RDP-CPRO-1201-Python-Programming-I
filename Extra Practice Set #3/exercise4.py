def count_vowels(s):
    counter = 0
    for i in s:
        if i.lower() in "aeiou":
            counter += 1
    return counter


print(count_vowels("Aello World!"))
