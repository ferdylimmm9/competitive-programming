# https://codeforces.com/contest/1985/problem/C
t = int(input())

while(t):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    temp = 0
    res = 0
    mx = 0
    for i in arr:
        temp+=i
        if(i >= mx):
            mx = i
            if(temp - mx == i):
                res+=1
        else:
            if(temp - mx == mx):
                res+=1
    print(res)    
        

    t = t-1