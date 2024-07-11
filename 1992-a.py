# https://codeforces.com/contest/1992/problem/A
t = int(input())

while(t):
    a,b,c = [int(x) for x in input().split(' ')]
    for i in range(5):
        n = min([a,b,c])
        if(a == n):
            a+=1
        elif(b == n):
            b+=1
        else:
            c+=1
    print(a*b*c)
    t = t - 1