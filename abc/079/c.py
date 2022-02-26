def main():
    A, B, C, D = [ int(i) for i in input() ]

    O = {
        '0': '-',
        '1': '+'
    }

    for i in range(8):
        ops = format(i, 'b').zfill(3)
        res = A
        
        if ops[0] == '0':
            res -= B
        else:
            res += B

        if ops[1] == '0':
            res -= C
        else:
            res += C

        if ops[2] == '0':
            res -= D
        else:
            res += D

        if res == 7:
            print(f'{A}{O[ops[0]]}{B}{O[ops[1]]}{C}{O[ops[2]]}{D}=7')
            return

if __name__ == '__main__':
    main()
