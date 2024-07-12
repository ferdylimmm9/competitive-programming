# https://codeforces.com/contest/1971/problem/B
t = int(input())

for _ in range(t):
    word = input()
    a = {}
    for i in range(len(word)):
        element = word[i]
        if(element in a):
            a[element] +=1
        else:
            a[element] = 1
    if(len(a) == 1):
        print("NO")
    else:
        print("YES")
        wrap = ''
        for x in a:
            wrap+= a[x]*x
        print(wrap[::-1])