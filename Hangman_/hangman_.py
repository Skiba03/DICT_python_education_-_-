import random


def start_game():
    print("HANGMAN\nThe game will be available soon.")
    t = 0
    a = ['python', 'java', 'javascript', 'php', ]
    r = (random.choice(a))
    m = '_' * len(r)
    while t <= 7:
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
                    print("Your word is", r, "\nYou win!\nThanks for playing!")
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
            t -= 1
        if t == 8:
            print("Your word is", r, "\nYou lose!\nThanks for playing!")
            break


def game_1():
    n = input('Type "play" to play the game, "exit" to quit:')
    if n == "play":
        start_game()
    elif n == "exit":
        return game_1()
    else:
        return game_1()


game_1()
