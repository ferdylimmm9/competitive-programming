# https://codeforces.com/problemset/problem/1987/A

t = int(input())

for _ in range(t):
    n,k = [int(x) for x in input().split(' ')]
    if(n == 1):
        print(1)
        continue
    if(k == 1):
        print(n)
        continue
    print(((n-1)*k)+1)