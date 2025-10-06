RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

h, w = 20, 30
cx, cy = w // 2, h // 2
r = 6
#ур.окр
def f(x, y):
    return (x - cx)**2 + (y - cy)**2 <= r**2

for y in range(h):
    for x in range(w):
        if f(x, y):
            print(f"{RED}  {END}", end="")
        else:
            print(f"{WHITE}  {END}", end="")
    print()
print("task2")
B = '\u001b[40m'
W = WHITE
E = END

h, w = 15, 40
R = 7

for y in range(h):
    for x in range(w):
        d1 = abs(x - 10) + abs(y - 7)
        d2 = abs(x - 25) + abs(y - 7)
        if d1 == R or d2 == R:
            print(f"{B}  {E}", end="")
        else:
            print(f"{W}  {E}", end="")
    print()
print('task3')
for y in range(h, -1, -1):
        for x in range(w + 1):
            if 3*x== y:
                print(f"{RED} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
        print()
true=sum(float(x)<-5 for x in open('sequence.txt'))
len=sum(float(x)<=0 for x in open('sequence.txt'))
print(f'{true*100/len}%[{RED}{' '*true}{END}{'-'*(len-true)}]')
