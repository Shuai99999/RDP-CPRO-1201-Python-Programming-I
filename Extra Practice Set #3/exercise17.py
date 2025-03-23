def word_frequency(sentence):
    word_count = {}

    for word in sentence:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


print(word_frequency("sentence"))
