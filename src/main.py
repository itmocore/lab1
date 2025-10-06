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
