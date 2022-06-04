from random import choice

mark = 0
count = 0
znak = 0.
a = 0
b = 0
c = 0
d = 1
f = 0
s = 0
level = 0


def stage_1():
    global a, f, c
    if d == 1:
        a = choice(range(2, 10))
        f = choice(range(2, 10))
        c = choice(['+','-','*'])


def level_2():
    global s,znak
    s =choice(range(11,30))
    znak = s ** 2
    print(s)


def stage1():
    stage_1()
    global znak, a, b, c
    if c == '+':
        print(str(a) + '+' + str(f))
        znak = a + f
    elif c == '-':
        print(str(a) + '-' + str(f))
        znak = a - f
    elif c == '*':
        print(str(a) + '*' + str(f))
        znak = a * f


def otvet():
    global d,count,mark
    if znak == answer:
        print("Right")
        mark += 1
        count += 1
        d = 1
    else:
        print("Wrong")
        count += 1
        d = 1


while level not in [1,2]:
    try:
        print("Which level do you want? Enter a number(1-eazy,2-difficult):")
        level = int(input())
    except ValueError:
        print("Incorrect format")


while count != 5:
    try:
        if level == 1:
            stage1()
            answer = int(input())
            otvet()
        elif level == 2:
            level_2()
            answer = int(input())
            otvet()
    except ValueError:
        print('Incorrect format')
        d = 0
print("Your mark is "+ str(mark) +"/5")
print("Would you like to save the result? Enteryes or no")
answer_file = input()
if answer_file == 'y' or 'YES' or 'Yes' or 'yes':
    name = input('What is your name?')
    file = open('results.txt','w')
    file.write(name + ':' + str(mark) + '/5' + 'in level' + str(level) + '/n')
    file.close()
    print('The results are saved in "results.txt"')