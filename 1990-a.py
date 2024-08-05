# https://codeforces.com/contest/1990/problem/A
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    setArr = list(set(arr))
    win = False
    for x in setArr:
        if(arr.count(x)%2 == 1):
            win = True
            break
    if(win):
        print("YES")
    else:
        print("NO")
