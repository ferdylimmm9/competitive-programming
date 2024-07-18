# https://codeforces.com/problemset/problem/1982/A

t = int(input())

for _ in range(t):
    a,b = [int(x) for x in input().split(' ')]
    a1,b1 = [int(x) for x in input().split(' ')]
    if(a > b and a1 > b1):
        print("YES")
    elif(a < b and a1 < b1):
        print("YES")
    elif(b == b1 and b == 0):
        print("YES")
    elif(a == a1 and  a == 0):
        print("YES")
    else:
        print("NO")