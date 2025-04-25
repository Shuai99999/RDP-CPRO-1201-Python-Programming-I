def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(sentence.lower()))


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("hello this is me"))
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
