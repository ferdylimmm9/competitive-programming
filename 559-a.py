# https://codeforces.com/contest/599/problem/A

d1,d2,d3 = map(int,input().split())

a = d1 + d2 + d3
b = 2*d1 + 2*d2
c = 2*d1 + 2*d3
d = 2*d2 + 2*d3
print(min(a,b,c,d))
