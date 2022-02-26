def main():
    N = int(input())

    ans = 0

    for n in range(1,N+1):
        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1

        if cnt == 8 and n % 2 == 1:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
