b = 0
c =' '
t = input("Enter cells:")
print("---------")
print("| " + t[0] + ' ' + t[1] + ' ' + t[2] + " |")
print("| " + t[3] + ' ' + t[4] + ' ' + t[5] + " |")
print("| " + t[6] + ' ' + t[7] + ' ' + t[8] + " |")
print("---------")
a = []
if str(t[0]) == str(t[1]) == str(t[2]) != c:
    b += 1
if str(t[3]) == str(t[4]) == str(t[5]) != c:
    b += 1
if str(t[6]) == str(t[7]) == str(t[8]) != c:
    b += 1
if str(t[0]) == str(t[3]) == str(t[6]) != c:
    b += 1
if str(t[1]) == str(t[4]) == str(t[7]) != c:
    b += 1
if str(t[2]) == str(t[5]) == str(t[8]) != c:
    b += 1
if str(t[0]) == str(t[4]) == str(t[8]) != c:
    b += 1
if str(t[6]) == str(t[4]) == str(t[2]) != c:
    b += 1
elif b == 2:
    print("Impossible")
    quit()
if str(t[0]) == str(t[1]) == str(t[2]) != c:
    print(t[0], "You wins")
    b += 1
    quit()
if str(t[3]) == str(t[4]) == str(t[5]) != c:
    print(t[3], "You wins")
    b += 1
    quit()
if str(t[6]) == str(t[7]) == str(t[8]) != c:
    print(t[6], "You wins")
    b += 1
    quit()
if str(t[0]) == str(t[3]) == str(t[6]) != c:
    print(t[0], "You wins")
    b += 1
    quit()
if str(t[1]) == str(t[4]) == str(t[7]) != c:
    print(t[1], "You wins")
    b += 1
    quit()
if str(t[2]) == str(t[5]) == str(t[8]) != c:
    print(t[2], "You wins")
    b += 1
    quit()
if str(t[0]) == str(t[4]) == str(t[8]) != c:
    print(t[0], "You wins")
    b += 1
    quit()
if str(t[6]) == str(t[4]) == str(t[2]) != c:
    print(t[6], "You wins")
    b += 1
    quit()
o = t.count('O')
x = t.count('X')
if o == 0 and x == 2 or o == 1 and x == 3 or o == 2 and x == 4 or o == 3 and x == 5 or o == 4 and x == 6:
    print("Impossible")
    quit()
if o == 5 and x == 7 or o == 6 and x == 8 or o == 7 and x == 9:
    print("Impossible")
    quit()
if x == 0 and o == 2 or x == 1 and o == 3 or x == 2 and o == 4 or x == 3 and o == 5 or x == 4 and o == 6:
    print("Impossible")
    quit()
if x == 5 and o == 7 or x == 6 and o == 8 or x == 7 and o == 9:
    print("Impossible")
    quit()
if c not in t:
    if len(a) == 0:
        print("Draw")
if c in t and b == 1:
    if len(a) == 0:
        print("Game not finished")
else:
    print("Game not finished")
    