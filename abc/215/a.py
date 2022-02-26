def main():
    N = int(input())

    for k in range(1000):
        if 2**k > N:
            print(k-1)
            return 
    

main()
#print(main())
