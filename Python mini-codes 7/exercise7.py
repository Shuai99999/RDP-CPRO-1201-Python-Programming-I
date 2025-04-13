def reverse_sentence(sentence):
    words = []
    word = ""
    i = 0

    while i < len(sentence):
        if sentence[i] != " ":
            word += sentence[i]
        else:
            if word:
                words.append(word)
                word = ""
        i += 1

    if word:
        words.append(word)

    reversed_sentence = ""

    for i in words[::-1]:
        reversed_sentence += i + " "
    reversed_sentence = reversed_sentence.strip()

    return reversed_sentence


def sentence_reverser():
    sentence = input("Enter a sentence: ")
    result = reverse_sentence(sentence)
    print("Reversed sentence:", result)


sentence_reverser()
