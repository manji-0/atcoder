def main():
    t = int(input())

    print(f(f((f(t)+t))+f(f(t))))

def f(t):
    return t**2 + 2*t + 3

if __name__ == '__main__':
    main()
