def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    ans = 3 ** N - 2 ** len([ i for i in A if i % 2 == 0 ])

    print(ans)


if __name__ == '__main__':
    main()
