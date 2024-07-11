# https://codeforces.com/problemset/problem/231/A
n = int(input())
result = 0
for _ in range(n):
    total = sum([int(x) for x in input().split(' ')])
    if(total >= 2):
        result +=1

print(result)