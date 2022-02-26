def main():
    S = list(input())
    K = int(input())

    R = [0] * len(S)

    for i in range(len(S)-1):
        if S[i] == ".":
            R[i+1] = R[i] + 1
        else:
            R[i+1] = R[i]

    ans = 0
    r = 0

    for l in range(len(S)):

        while r < len(S)-1 and R[r+1] - R[l] <= K:
            r += 1


        print(S[l:r+1])
        print(R[l:r+1])

        ans = max(ans, len(S[l:r+1]))

    print(ans)

if __name__ == '__main__':
    main()
