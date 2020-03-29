n = int(input())
# a,b = map(int,input().split())
# A = list(map(int,input().split()))
# An = [list(map(int,input().split())) for i in range(n)]
a = n//500
b = (n-a*500)//5
ans = int(a*1000 + b*5)
print(ans)