def main():
    S = list(input())
    K = int(input())

    if len(S) < K:
        print(0)
        return

    candidate = set()

    for i in range(len(S)-K+1):
        candidate.add("".join(S[i:i+K]))

    print(len(candidate))

main()
#print(main())
