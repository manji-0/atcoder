from audioop import avg
from math import sqrt, ceil

def main():
    x1,y1,x2,y2 = [ int(i) for i in input().split() ]

    if ((x1-x2)**2 + (y1-y2)**2) > 20:
        print("No")
        return

    xs = (x1+x2)//2 - ceil(sqrt(5))
    xe = (x1+x2)//2 + ceil(sqrt(5))

    ys = (y1+y2)//2 - ceil(sqrt(5))
    ye = (y1+y2)//2 + ceil(sqrt(5))

    for x in range(xs,xe+1):
        for y in range(ys,ye+1):
            a = (x1-x)**2 + (y1-y)**2
            b = (x2-x)**2 + (y2-y)**2

            if a == b == 5:
                print("Yes")
                return

    print("No")

main()
#print(main())
