# sentence = "Find the most repeated character in a sentence."
sentence = "Write a Python code that receives a string and removes all the spaces from that string."
distinct_letters = set(sentence.lower().replace(" ", ""))
max_letter_time = 0
max_letter = ""
for i in distinct_letters:
    # this_letter_time = sentence.count(i)
    this_letter_time = 0
    for j in sentence.lower():
        if i == j:
            this_letter_time += 1
    if this_letter_time > max_letter_time:
        max_letter_time = this_letter_time
        max_letter = i
print(f"The max letter is {max_letter}, it appears {max_letter_time} times.")
