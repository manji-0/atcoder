from collections import deque

def main():
    n = int(input())
    P = [ int(i) for i in input().split() ]

    Pr = deque(P)
    Pl = deque(P)

    countR = 0
    countL = 0

    while Pr[0] != 1:
        Pr.appendleft(Pr.pop())
        countR += 1

    

if __name__ == '__main__':
    main()
