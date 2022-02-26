def main():
    X = int(input())

    if X >= 0:
        print(X//10)
    else:
        X = -1 * X
        print("-"+str((X+9)//10))


main()
#print(main())
