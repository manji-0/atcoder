from collections import defaultdict

def main():
    N = int(input())
    Bd = defaultdict(int)
    
    for _ in range(N):
        Bd[input()] += 1

    M = int(input())
    Rd = defaultdict(int)

    for _ in range(M):
        Rd[input()] += 1

    ans = 0

    for k in Bd:
        Bd[k] = Bd[k] - Rd.get(k, 0)
        ans = max(ans, Bd[k])
    
    print(ans)

if __name__ == '__main__':
    main()
