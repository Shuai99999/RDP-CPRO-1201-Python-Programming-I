zodiac_signs = [
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
]

year = int(input("Input your birth year: "))

index = (year - 1900) % 12

print("Your Zodiac sign:", zodiac_signs[index])
