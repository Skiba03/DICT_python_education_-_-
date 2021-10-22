print("Hello! My name is BOT.\nI was created in 2021.")
a = input("Please remind me your name.")
print("What a great name you have,",a)
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3,5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that`s a good time to start programming.")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
for i in range(number):
    print(i, end="!\n")
print("Let`s test your programming knowledge.")
print("Why do use methods?")
print("1.To repeat a statement multiple times.\n2.To decompose a program into several small subroutines.")
print("3.To determine the execution time of a program.\n4.To interrupt the execution of a program.")
while True:
    user_text = input("")
    if user_text  == '2':
        break
    else:
        print("Please,try again.")
print("Completed,have a nice day.\nCongratulations,have a nice day.")









