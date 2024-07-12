# https://codeforces.com/contest/1971/problem/A

t = int(input())

for _ in range(t):
    x,y = [int(x) for x in input().split(' ')]
    if(x > y):
        x,y = y,x
    print(x,y)