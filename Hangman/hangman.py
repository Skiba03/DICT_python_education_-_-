print("HANGMAN\nThe game will be available soon.")
while True:
    import random

    a = ['python', 'java', 'javascript', ]
    r = (random.choice(a))
    w = (r[:3] + "-" * (len(r) - 3))
    words = input("HANGMAN\nGuess the word "+ w +":")
    if words == r:
        break
    else:
        print("You lost!")
print("You survived!")