sentence = input("Enter a sentence: ")
upper_count = sum(1 for c in sentence if c.isupper())
lower_count = sum(1 for c in sentence if c.islower())
print(f"Uppercase letters: {upper_count}, Lowercase letters: {lower_count}")
