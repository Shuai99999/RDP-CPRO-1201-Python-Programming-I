message = input("Please input a message: ")
spy_words = ["Morris", "RDP", "ENCP"]
for i in spy_words:
    reversal_word = i[::-1]
    if i in message or reversal_word in message:
        print("You are a spy!")
        break
else:
    print("You are not a spy.")
