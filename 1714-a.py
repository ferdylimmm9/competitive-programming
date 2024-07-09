# https://codeforces.com/contest/1714/problem/A
highMinutes = 24*60
def solve():
    n,h,m = [int(x) for x in input().split(' ')]
    times = h*60+m
    highest = 24*60
    for i in range(n):
        hi,mi = [int(x) for x in input().split(' ')]
        temp = hi*60+mi
        result = temp - times
        if(result < 0):
            result += highMinutes
        highest = min(result, highest)
    print (highest//60, highest%60)
t = int(input())

while(t):
    solve()
    t = t - 1