t = int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split(' ')]
    step = 1
    for i in range(1,n+1):
        row = input()
        if(i%(k*step)==0):
            print(row[::k])