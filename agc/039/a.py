def main():
    S = list(input())
    K = int(input())

    cnt = 0

    if S[0] == S[-1]:
        cnt += 1
        S.pop()

    i = 0
    j = 1
    tmp = 1

    while i < len(S) and j < len(S):
        if S[i] == S[j]:
            tmp += 1
            j += 1
        else:
            cnt += tmp//2
            tmp = 1
            i = j
            j = i+1

    print(cnt*K)

if __name__ == '__main__':
    main()
