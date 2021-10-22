print("HANGMAN\nThe game will be available soon.")
while True:
    words = input("HANGMAN\nGuess the word:")
    import random

    a = ['python', 'java', 'javascript', ]
    if words == ( random.choice(a)):
        break
    else:
        print("You lost!")
print("You survived!")