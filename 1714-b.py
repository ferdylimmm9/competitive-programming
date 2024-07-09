# https://codeforces.com/contest/1714/problem/B
def solve():
    n = int(input())
    row = input().split(' ')[::-1]
    length = len(row)
    sa = set()
    if(n == 1):
        return 0
    for i in range(length):
        element = row[i]
        if(element in sa):
            break
        sa.add(element)
    return length - len(sa)
t = int(input())
while(t):
    print(solve())
    t = t - 1
