# https://codeforces.com/contest/1985/problem/D
t = int(input())

while(t):
    x, y= [int(x) for x in input().split(" ")]
    start = 0
    end = 0
    mx = 0
    found = False
    for i in range(x):
        row = input()
        trim = row.count("#")
        if(trim > mx):
            mx = trim
            end = i+1
        if(found):
            continue
        if(trim == 1):
            for j in range(len(row)):
                if(row[j] == '#'):
                    start = j+1
                    found = True
    print(end,start)
        
    t = t-1