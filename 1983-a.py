# https://mirror.codeforces.com/contest/1983/problem/A

t = int(input())

for _ in range(t):
    print(*[i for i in range(1, int(input())+1)])