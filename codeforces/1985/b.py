# https://codeforces.com/contest/1985/problem/B

t = int(input())

while(t):
    n = int(input())
    mx = 0
    res = 0
    for i in range(2,n+1):
        div = n // i 
        sumResult = (div*(div+1))//2
        sumMulti = sumResult * i
        if(mx < sumMulti):
            mx = sumMulti
            res = i
    print(res)
    t = t-1

# i use arithmetic progression