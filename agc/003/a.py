def main():
    S = input()

    D = set()

    for d in S:
        D.add(d)

    if "S" in D:
        if "N" not in D:
            print("No")
            return
    if "N" in D:
        if "S" not in D:
            print("No")
            return
    if "W" in D:
        if "E" not in D:
            print("No")
            return
    if "E" in D:
        if "W" not in D:
            print("No")
            return
    
    print("Yes")

if __name__ == '__main__':
    main()
