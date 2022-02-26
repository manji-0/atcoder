def main():
    N = int(input())
    R = list(input())

    ans = 0

    for r in R:
        if r == "A":
            ans += 4
        elif r == "B":
            ans += 3
        elif r == "C":
            ans += 2
        elif r == "D":
            ans += 1
    
    ans = ans / N

    print(ans)

if __name__ == '__main__':
    main()
