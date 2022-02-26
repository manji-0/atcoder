def main():
    N = int(input())

    if 2**31 > N >= -1*2**31:
        print("Yes")
    else:
        print("No") 

main()
