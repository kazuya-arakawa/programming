# n = int(input())
r,d,x = map(int,input().split())
# A = list(map(int,input().split()))
# An = [list(map(int,input().split())) for i in range(n)]

for __ in range(10):
    x = r*x - d
    print(x)