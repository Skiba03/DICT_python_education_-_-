print("HANGMAN\nThe game will be available soon.")
while True:
    user_text = input("HANGMAN\nGuess the word:")
    if user_text  == 'python':
        break
    else:
        print("You lost!")
print("You survived!")

