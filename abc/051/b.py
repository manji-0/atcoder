def main():
    K, S = [ int(i) for i in input().split() ]

    ans = 0

    for x in range(K+1):
        for y in range(K+1):
            if S-x-y > K:
                continue
            ans += 1 if S-x-y >= 0 else 0

    print(ans)

if __name__ == '__main__':
    main()
