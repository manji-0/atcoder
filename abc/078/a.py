def main():
    X, Y = input().split()

    if ord(X) > ord(Y):
        print(">")
    elif ord(X) < ord(Y):
        print("<")
    else:
        print("=")

if __name__ == '__main__':
    main()
