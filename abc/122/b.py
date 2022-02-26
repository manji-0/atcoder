def main():
    S = list(input())
    acgt = ['A','C', 'G', 'T']
    ans = 0

    for i in range(0,len(S)):
        if S[i] not in acgt:
            continue
        l = 1

        for j in range(i+1, len(S)):
            if S[j] not in acgt:
                break

            l += 1
        
        ans = max(ans,l)

    print(ans)

if __name__ == '__main__':
    main()
