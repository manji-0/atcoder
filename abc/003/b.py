def main():
    S = input()
    T = input()

    for i in range(len(S)):
        if S[i] == '@' and T[i] in "atcoder":
            pass
        elif T[i] == '@' and S[i] in "atcoder":
            pass
        elif S[i] != T[i]:
            print("You will lose")
            return
    
    print("You can win")

main()
#print(main())
