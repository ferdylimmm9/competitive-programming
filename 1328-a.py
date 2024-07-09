# https://codeforces.com/contest/1328/problem/A
def solve():
    a,b = [int(x) for x in input().split(' ')]
    if(a%b == 0):
        return 0
    else:
        return(b - (a%b))
t = int(input())
while(t):
    print(solve())
    t = t - 1