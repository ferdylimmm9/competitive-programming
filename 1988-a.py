t = int(input())

for _ in range(t):
    n,k = [int(x) for x in input().split(' ')]
    operation = 0
    while(n > 1):
        n -= (k-1)
        operation = operation + 1
    print(operation)

