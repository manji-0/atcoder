def main():
    T = int(input())
    C = [ [ int(i) for i in input().split() ] for _ in range(T) ]

    for a,s in C:
        if 2*a > s:
            print("No")
            continue
        if bin((s-a)&a) == bin(a):
            print("Yes")
        else:
            print("No")

main()
#print(main())
