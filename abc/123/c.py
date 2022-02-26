def main():
    N = int(input())
    T = [ int(input()) for _ in range(5) ]

    miT = min(T)
    
    if miT >= N:
        print(5)
        return

    ans = N // miT if (N/miT <=  N // miT) else  N // miT + 1

    print(4+ans)

    

if __name__ == '__main__':
    main()
