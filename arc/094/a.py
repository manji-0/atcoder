def main():
    T = [ int(i) for i in input().split() ]

    T.sort()

    ans = T[2] - T[1]

    if (T[1] - T[0]) % 2 == 0:
        ans += (T[1] - T[0]) // 2
    else:
        ans += (T[1] - T[0]) // 2
        if ((T[1]-T[0]) / 2 - (T[1] - T[0]) // 2) > 0:
            ans += 1
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
