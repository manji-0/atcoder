def main():
    N = int(input())
    R = list(input())

    w = 0
    e = 0
    ans = N

    for r in R:
        if r == "W":
            w += 1
        else:
            e += 1

    ww = 0
    ee = 0
    for r in R:
        if r == "W":
            w -= 1
            ans = min(ans, e+ww)
            ww += 1
        else:
            e -= 1
            ans = min(ans, e+ww)
            ee += 1
    
    print(ans)
    

if __name__ == '__main__':
    main()
