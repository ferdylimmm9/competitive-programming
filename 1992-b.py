# https://codeforces.com/contest/1992/problem/B

t = int(input())

while(t):
    n,k = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    a.sort()
    total = 0
    for i in range(len(a)-1):
        element = a[i]
        if(element == 1):
            total +=1
        else:
            total += element + element - 1
    print(total)
    t = t - 1