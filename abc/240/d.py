from collections import defaultdict

def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    S = 0
    Bl = [dict()]

    for a in A:
        S += 1

        if Bl[-1].get(a):
            if Bl[-1][a] == a-1:
                S -= a
                del Bl[-a+1:]
            else:
                Bl.append({a: Bl[-1][a]+1})
        else:
            Bl.append({a: 1})

        print(S)

main()
#print(main())
