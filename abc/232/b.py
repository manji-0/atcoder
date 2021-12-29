
def main():
    S = input()
    T = input()

    if S == T:
        print('Yes')
        return

    base = diff(S[0], T[0])

    for s, t in zip(S[1:], T[1:]):
        if diff(s, t) != base:
            print('No')
            return

    print('Yes')

def diff(s, t):
    d = ord(t) - ord(s)
    
    if d == 0:
        return d

    d = max(d, 26-d)

    return d

if __name__ == "__main__":
    main()
