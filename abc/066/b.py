def main():
    S = list(input())
    S.pop()
    S = "".join(S)

    ans = 0

    for i in range(len(S)):
        s = S[0:i+1] + S[0:i+1]

        if S.startswith(s):
            ans = max(ans, len(s))

    print(ans)    

if __name__ == '__main__':
    main()
