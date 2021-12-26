print('---------')
print("| _ _ _ |")
print("| _ _ _ |")
print("| _ _ _ |")
print('---------')
print('Enter cells:')
a = list(input())
lin = str('---------')
b_1 = ['|', a[0], a[1], a[2], '|']
b_2 = ['|', a[3], a[4], a[5], '|']
b_3 = ['|', a[6], a[7], a[8], '|']
s_b = [' ', b_1, b_2, b_3, ' ']
rang = [int(i) for i in range(1, 4)]
error1 = 0
error2 = 0
v = 0


def wins():
    vvod = []
    if a.count("X") - a.count("O") >= 2:
        return "Impossible"
    elif a.count("O") - a.count("X") >= 2:
        return "Impossible"
    if b_1[1] == b_1[2] == b_1[3] != '_':
        vvod.append(b_1[1])
    if b_2[1] == b_2[2] == b_2[3] != '_':
        vvod.append(b_2[1])
    if b_3[1] == b_3[2] == b_3[3] != '_':
        vvod.append(b_3[1])
    if b_1[1] == b_2[1] == b_3[1] != '_':
        vvod.append(b_1[1])
    if b_1[2] == b_2[2] == b_3[2] != '_':
        vvod.append(b_1[2])
    if b_1[3] == b_2[3] == b_3[3] != '_':
        vvod.append(b_1[3])
    if b_1[1] == b_2[2] == b_3[3] != '_':
        vvod.append(b_1[1])
    if b_1[3] == b_2[2] == b_3[1] != '_':
        vvod.append(b_1[3])
    if vvod.count('X') >= 2:
        vvod.remove('X')
    elif vvod.count('O') >= 2:
        vvod.remove('O')
    if len(vvod) >= 2:
        return "Impossible"
    elif len(vvod) == 1:
        return vvod[0] + ' wins'
    elif '_' not in a:
        if len(vvod) == 0:
            return "Draw"
    elif '_' in a:
        if len(vvod) == 0:
            return "Game not finished"


def pole():
    print(lin)
    print(' '.join(b_1))
    print(' '.join(b_2))
    print(' '.join(b_3))
    print(lin)
    print(wins())


def error():
    c = 0
    global b_1, b_2, b_3, error1, error2, v, a
    while c != 1:
        v += 1
        print('Enter the coordinates:')
        try:
            error1, error2 = input().split(' ')
            error1 = int(error1)
            error2 = int(error2)
        except ValueError:
            v -= 1
            print('You should enter numbers!')
            continue
        if error1 and error2 not in rang:
            print('Coordinates should be from 1 to 3!')
            v -= 1
        elif error1 and error2 in rang:
            if s_b[error1][error2] != '_':
                v -= 1
                print('This cell is occupied! Choose another one!')
            else:
                if v % 2 == 1:
                    s_b[int(error1)][int(error2)] = 'X'
                    if error1 == 1:
                        a[error2 - error1] = 'X'
                    elif error1 == 2:
                        a[error1 + error2] = 'X'
                    else:
                        a[error1 + error2 + 2] = 'X'
                    c = 1
                else:
                    s_b[int(error1)][int(error2)] = 'O'
                    if error1 == 1:
                        a[error2 - error1] = 'O'
                    elif error1 == 2:
                        a[error1 + error2] = 'O'
                    else:
                        a[error1 + error2 + 2] = 'O'
                    c = 1
    pole()


pole()
while wins() == 'Game not finished':
    error()
