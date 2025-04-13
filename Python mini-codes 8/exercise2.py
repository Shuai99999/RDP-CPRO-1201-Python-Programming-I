import random

names = ["Alice", "Bob", "Charlie", "Diana"]
pronouns = ["he", "she", "they", "it"]
verbs = ["eats", "likes", "builds", "destroys", "paints", "throws"]
adjectives = ["happy", "red", "fast", "weird", "loud", "funny"]
nouns = ["car", "banana", "house", "robot", "song", "book"]


def generate_sentence():
    subject = random.choice(names)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    obj = random.choice(nouns)
    return f"{subject} {verb} the {adjective} {obj}."


def main():
    sentences = []
    print("Generated Sentences:\n")
    for i in range(10):
        sentence = generate_sentence()
        sentences.append(sentence)
        print(f"{i+1}. {sentence}")

    print()
    count = input("How many of these 10 sentences make sense to you? ")
    print(f"\nYou think {count} out of 10 sentences make sense. Got it!")


if __name__ == "__main__":
    main()
