# https://codeforces.com/contest/158/problem/A

n,k = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]
arr.sort(reverse=True)
filtered = filter(lambda x: x >=arr[k-1] and x != 0, arr)
print(len(list(filtered)))