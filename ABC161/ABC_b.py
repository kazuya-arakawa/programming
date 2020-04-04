n,m = map(int,input().split())
A = list(map(int,input().split()))

s = sum(A)
A.sort(reverse=True)

if A[m-1] >= s*1/(4*m):
    print('Yes')
else:
    print('No')