def main():
    A,B,C = [ int(i) for i in input().split() ]

    if sum([ i % 2 for i in [A,B,C] ]) > 0:
        print(0)
        return

    if A == B == C:
        print(-1)
        return

    cnt = 0

    while sum([ i % 2 for i in [A,B,C] ]) == 0:
        tmp_a = B // 2 + C // 2
        tmp_b = A//2 + C//2
        tmp_c = A//2 + B//2

        A = tmp_a
        B = tmp_b
        C = tmp_c

        cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
