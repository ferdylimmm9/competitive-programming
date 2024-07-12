# https://codeforces.com/contest/1971/problem/C
t = int(input())

for _ in range(t):
    a,b,c,d = [int(x) for x in input().split(' ')]
    if(a < b):
        a,b = b,a
    if(c<d):
        c,d = d,c
    if(a - b == 1 or c - d == 1):
        print("NO")
        continue
    lower = list(range(b,a))
    if(d in lower):
        if(c in lower):
            print("NO")
        else:
            print("YES")
    else:
        if(c in lower):
            print("YES")
        else:
            print("NO")
    
