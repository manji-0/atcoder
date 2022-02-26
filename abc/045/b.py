def main():
    Sa = list(input())
    Sb = list(input())
    Sc = list(input())
    Sa.reverse()
    Sb.reverse()
    Sc.reverse()

    T = Sa
    P = "A"

    while True:
        if len(T) == 0:
            print(P)
            return
        t = T.pop()

        if t == "a":
            T = Sa
            P = "A"
        elif t == "b":
            T = Sb
            P = "B"
        else:
            T = Sc
            P = "C"

if __name__ == '__main__':
    main()
