def main():
    K = int(input())

    bK = list(bin(K)[2:].lstrip("0"))

    ans = []

    for i in bK:
        if i == "0":
            ans.append(0)
        else:
            ans.append(2)

    print(*ans, sep="")

if __name__ == '__main__':
    main()
