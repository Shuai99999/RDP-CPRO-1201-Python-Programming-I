def count_words_starting_with(words, letter):
    return sum(1 for word in words if word.startswith(letter))


words_list = [
    "cloud",
    "calm",
    "wonder",
    "capture",
    "crystal",
    "dawn",
    "dazzle",
    "whisper",
    "dream",
    "wavelength",
]
letter = "w"
print(count_words_starting_with(words_list, letter))
