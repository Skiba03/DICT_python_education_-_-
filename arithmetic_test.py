from random import choice

mark = 0
count = 0
znak = 0.
a = 0
b = 0
c = 0
d = 1

def stage_1():
    global a, b, c
    if d == 1:
        a = choice(range(2, 10))
        b = choice(range(2, 10))
        c = choice(['+','-','*'])


def stage1():
    stage_1()
    global znak, a, b, c
    if c == '+':
        print(str(a) + '+' + str(b))
        znak = a + b
    elif c == '-':
        print(str(a) + '-' + str(b))
        znak = a - b
    elif c == '*':
        print(str(a) + '*' + str(b))
        znak = a * b


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

while count != 5:
    try:
        stage1()
        answer = int(input())
        otvet()
    except ValueError:
        print('Incorrect format')
        d = 0
print("Your mark is "+ str(mark) +"/5")
