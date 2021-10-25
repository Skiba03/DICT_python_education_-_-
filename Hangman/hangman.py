import random
print("HANGMAN\nThe game will be available soon.")
t = 0
while t <= 7:
    a = ['python', 'java', 'javascript', 'php', ]
    r = (random.choice(a))
    # w = (r[:3] + "-" * (len(r) - 3))
    # words = input("HANGMAN\nGuess the word "+ w +":")
    m = '_' * len(r)
    words = input("" + m + "\nInput a letter:")
    while words:
        words = input("" + m + "\nInput a letter:")
        if words in r:
            print('That letter appear in the word')
            new = ''
            for i in range(len(r)):
                if words == r[i]:
                    new += words
                else:
                    new += m[i]
                if new == r:
                    print("You win!\nThanks for playing!")
                    quit()
            m = new
        else:
            print("That letter doesn't appear in the word")
        t += 1
        if t == 8:
            print("You lose!\nThanks for playing!")
            break

