from collections import defaultdict

def main():
    N = int(input())
    W = [ i for i in input().split() ]

    freq_1 = "init"
    freq_2 = "init"

    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for i in range(0, N, 2):
        count1[W[i]] += 1
        count2[W[i+1]] += 1

        if count1[W[i]] > count1[freq_1]:
            freq_1 = W[i]
        if count2[W[i+1]] > count2[freq_2]:
            freq_2 = W[i+1]

    s1 = 0
    s2 = 0

    for k, v in count1.items():
        if k == freq_1:
            continue

        s1 += v

    for k, v in count2.items():
        if k == freq_2:
            continue

        s2 += v

    print(s1+s2)

if __name__ == '__main__':
    main()
