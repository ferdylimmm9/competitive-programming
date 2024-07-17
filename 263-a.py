# https://codeforces.com/contest/263/problem/A

y = 0
x = 0
for i in range(5):
    col = input().split(' ')
    if(col.count('1') == 1):
        y = i
        x = col.index('1')
if(x > 2):
    x = x - 2
else:
    x = 2 - x
if(y > 2):
    y = y - 2
else:
    y = 2 - y
print(x+y)

