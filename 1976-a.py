# https://codeforces.com/problemset/problem/1976/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = [x for x in input()]
    temp = list(a)
    temp.sort()
    print("YES" if temp == a else "NO")