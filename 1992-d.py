# https://codeforces.com/contest/1992/problem/D

#NEED TO LEARN MORE
def MUKU():
    t = int(input().strip())  # Number of test cases
    
    results = []
    
    for _ in range(t):
        n, m, k = map(int, input().strip().split())
        str = input().strip()
        
        temp = m - 1
        x = 0
        y = 0
        
        for i in range(n):
            if str[i] == 'L':
                temp = m
            elif str[i] == 'W':
                if temp <= 0:
                    x += 1
            else:  # 'C'
                if temp <= 0:
                    y += 1
            
            temp -= 1
        
        if x > k:
            y += 1
        
        if y != 0:
            results.append("NO")
        else:
            results.append("YES")
    
    for result in results:
        print(result)

# Example usage
MUKU()

