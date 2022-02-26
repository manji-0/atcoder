def main():
    N, M = [ int(i) for i in input().split() ]

    ans = 100 * (N-M)
    ans += 1900 * M
    ans *= 2**M

    print(ans)

if __name__ == '__main__':
    main()
