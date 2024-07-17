# https://codeforces.com/contest/1984/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    if(arr[0] == arr[len(arr)-1]):
        print("NO")
    else:
        pattern = ['R']*n
        pattern[1] = 'B'
        print("YES")
        print(''.join(pattern))
