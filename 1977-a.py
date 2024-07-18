# https://codeforces.com/problemset/problem/1977/A

t  = int(input())

for _ in range(t):
    n,m = [int(x) for x in input().split(' ')]
    if(n < m):
        print("NO")
    else:
        if((n - m)%2 == 0):
            print("YES")
        else:
            print("NO")