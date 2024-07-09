## https://codeforces.com/contest/1985/problem/A
n = int(input())

for i in range(n):
    a,b = input().split(' ')
    print(b[0]+a[1]+a[2],a[0]+b[1]+b[2])