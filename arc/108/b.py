def main():
    N = int(input())
    S = list(input())

    S.reverse()
    t = []

    while True:
        if "".join(t[-3:]) == "fox":
            t.pop()
            t.pop()
            t.pop()
        else:
            if S:
                c = S.pop()
                t.append(c)
            else:
                break

    print(len(t))

main()
#print(main())
