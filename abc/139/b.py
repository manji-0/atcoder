def main():
    A, B = [ int(i) for i in input().split() ]

    S = 1
    ans = 0

    while B > S:
        S -= 1
        S += A
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
