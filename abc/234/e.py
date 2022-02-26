def main():
    X = input()
 
    if int(X) < 100:
        print(X)
        return
 
    ma = 1 + 10 // len(X)
    ans = 10**19
    
    for a in arinum(len(X), ma):
        if a < int(X):
            continue
 
        ans = min(ans, a)
 
    print(ans)
 
def arinum(n, a):
    for i in range(1,10):
        for j in range(-a, a+1):
            ans = [str(i)]
            k = i
            while len(ans) < n:
                k += j           
 
                if 0<=k<=9:
                    ans.append(str(k))
                else:
                    break
            
            if len(ans) == n:
                yield int("".join(ans))
            else:
                continue
 
if __name__ == '__main__':
    main()