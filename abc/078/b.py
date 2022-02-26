def main():
    X, Y, Z = [ int(i) for i in input().split() ]

    ans = (X-Z) // (Y+Z)

    print(ans)

if __name__ == '__main__':
    main()
