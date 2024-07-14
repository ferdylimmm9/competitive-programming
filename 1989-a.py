# https://codeforces.com/problemset/problem/1989/A

t = int(input())

for _ in range(t):
    x,y = [int(x) for x in input().split(' ')]
    if(y > -2):
        print("YES")
    else:
        print("NO")
