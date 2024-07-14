# https://codeforces.com/problemset/problem/1986/A

t = int(input())

for _ in range(t):
    x1,x2,x3 = [int(x) for x in input().split(' ')]
    res1 = abs(x1-x1) + abs(x2 - x1) + abs(x3 - x1)
    res2 = abs(x1-x2) + abs(x2 - x2) + abs(x3 - x2)
    res3 = abs(x1-x3) + abs(x2 - x3) + abs(x3 - x3)
    result = min(res1,res2,res3)
    print(result)