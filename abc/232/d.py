def main():
    H, W = [ int(i) for i in input().split() ]

    C = [ list(input()) for _ in range(H) ]

    stack = []

    stack.append((0, 0, 1))
    ma = 0
    visited = set()

    while stack:
        h, w, l = stack.pop()

        if (h,w) in visited:
            continue
        else:
            visited.add((h,w))

        if l > ma:
            ma = l

        if h < H-1 and C[h+1][w] != '#':
            stack.append((h+1, w, l+1))

        if w < W-1 and C[h][w+1] != '#':
            stack.append((h, w+1, l+1))

    print(ma)

if __name__ == '__main__':
    main()
