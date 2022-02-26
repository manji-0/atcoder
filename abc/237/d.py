def main():
    N = int(input())
    S = list(input())

    cur = 0
    curItem = LinkedList(0)

    for s in S:
        cur += 1
        if s == "L":
            item = LinkedList(cur, pre=curItem.pre, next=curItem)

            if curItem.pre:
                curItem.pre.next = item

            curItem.pre = item
        else:
            item = LinkedList(cur, pre=curItem, next=curItem.next)

            if curItem.next:
                curItem.next.pre = item

            curItem.next = item

        curItem = item

    ans = []

    while 1:
        if curItem.pre is not None:
            curItem = curItem.pre
        else:
            break

    while 1:
        ans.append(curItem.value)
        curItem = curItem.next

        if not curItem:
            break
            

    print(*ans, sep=" ")

    

class LinkedList:
    def __init__(self, value, pre=None, next=None):
        self.value = value
        self.next = next
        self.pre = pre
    

main()
#print(main())
