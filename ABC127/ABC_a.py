# n = int(input())
a,b = map(int,input().split())
# A = list(map(int,input().split()))
# An = [list(map(int,input().split())) for i in range(n)]

if 13 <= a:
    print(b)
elif 6<= a <= 12:
    print(int(b/2))
else:
    print(0)