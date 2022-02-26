def main():
    S = list(input())

    if S == S[::-1]:
        print("Yes")
        return

    if S[-1] != "a":
        print("No")
        return

    scnt = 0
    tcnt = 0

    while S[-1] == "a":
        S.pop()
        tcnt += 1

    S = S[::-1]

    while S[-1] == "a":
        S.pop()
        scnt += 1

    if S == S[::-1] and scnt < tcnt:
        print("Yes")
        return

    print("No")
    

main()
#print(main())
