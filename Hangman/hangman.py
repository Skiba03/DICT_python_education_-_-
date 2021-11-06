import random

print("HANGMAN\nThe game will be available soon.")
t = 0
while t <= 7:
    a = ['python', 'java', 'javascript', 'php', ]
    r = (random.choice(a))
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
                if words in m[i]:
                    print("You have already entered this letter")
                    t -= 1
            m = new
        else:
            print("That letter doesn't appear in the word")
        t += 1
        y = words
        if y.isalpha():
            print()
        else:
            print("Please enter a lowercase English letter")
            t -= 1
        o = len(words)
        if o == 1:
            print()
        else:
            print("You should input a single letter")
        if t == 8:
            print("You lose!\nThanks for playing!")
            break
