# https://codeforces.com/problemset/problem/469/A
n = int(input())
x = input().split(' ')[1:]
y = input().split(' ')[1:]
all = set(x + y)
if(n == len(all)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")