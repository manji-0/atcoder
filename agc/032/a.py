def main():
    N = int(input())
    B = [ int(i) for i in input().split() ]

    ans = []

    while len(B) > 0:
        flag = True
        for i in range(len(B)-1,-1,-1):
            if B[i] == i+1:
                flag = False
                ans.append(i+1)
                B = B[0:i] + B[i+1:]
                break

        if flag:
            print(-1)
            return

    ans.reverse()

    print(*ans, sep="\n")

if __name__ == '__main__':
    main()
