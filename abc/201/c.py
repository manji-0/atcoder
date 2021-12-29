import math

def main():
    S = input()

    o = 0
    q = 0
    x = 0

    for s in S:
        if s == "o":
            o += 1
        elif s == "x":
            x += 1
        elif s == "?":
            q += 1

    if o > 4 or o == 0 and q == 0:
        print("0")
        return

    res = math.factorial(o) * (o+q) ** (4-o)

    print(res)

if __name__ == '__main__':
    main()
