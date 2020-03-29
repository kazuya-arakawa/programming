# n = int(input())
k,n = map(int,input().split())
A = list(map(int,input().split()))
# An = [list(map(int,input().split())) for i in range(n)]
d = []
for i in range(n-1):
    d.append(A[i+1]-A[i])
d.append(k-A[n-1]+A[0])
print(k-max(d))