def main():
    A, B = [ int(i) for i in input().split() ]

    if min(A,B) == 1 and max(A,B) == 10:
        print("Yes")
        return

    if abs(A-B) == 1:
        print("Yes")
    else:
        print("No")

main()
#print(main())
