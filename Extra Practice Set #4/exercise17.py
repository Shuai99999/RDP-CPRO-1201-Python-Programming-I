def calculate_dict(sentence):
    freq_dict = {}
    for i in sentence:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict


# print(calculate_dict("Ifjasdkf;adfarfm"))


def calculate_words(sentence):
    if sentence[0] != " ":
        num = 1
    else:
        num = 0

    for i in sentence:
        if i = ' ':
          

    # return num


print(calculate_words("  x x   x   x"))
# print(calculate_words("      "))
