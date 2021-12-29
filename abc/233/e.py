def main():
    X = list(input())

    s = 0

    for _ in range(10**100):
        s += int("".join(X))
        X.pop()

        if not X:
            break

    print(s)

if __name__ == '__main__':
    main()
