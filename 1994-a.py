# https://codeforces.com/contest/1994/problem/A

t = int(input())

for _ in range(t):
    n,m = [int(x) for x in input().split(' ')]
    arr = []
    for _ in range(n):
        col = [int(x) for x in input().split(' ')]
        arr.append(col)

    if(n == 1 and m == 1):
        print(-1)
    elif(n == 1 and m>1):
        for j in range(m):
            print(arr[n-1][(m+j+1)%m],end=" ")
        print()
    else:
        for i in range(n):
            for j in range(m):
                print(arr[(n+i+1)%n][(m+j+1)%m],end=" ")
            print()


