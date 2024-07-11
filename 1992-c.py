# https://codeforces.com/contest/1992/problem/C

t = int(input())

while(t):
    n,m,k = [int(x) for x in input().split(' ')]
    length = n//2
    low = list(range(1,m+1))
    high = list(range(n,k-1,-1))
    mid = list(range(m+1,k))
    print(*high,*mid,*low)
    t = t - 1