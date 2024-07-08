# https://codeforces.com/contest/1985/problem/E
def solve():
    x,y,z,k = [int(x) for x in input().split(' ')]
    total = 0
    for i in range(1,x+1):
        for j in range(1,y+1):
            if(k%(i*j) != 0):
                continue
            height = k//(i*j)
            if(height > z):
                continue
            total = max((x - i + 1) * (y - j + 1) * (z - height + 1),total)
    return total        
t = int(input())
while(t):
    print(solve())
    t = t - 1