# n = int(input())

# 再帰関数のお勉強
# def su(n):
#     if n < 1:
#         return 0
#     return n + su(n-1)

# def dil(l):
#     if l == []:
#         return []
#     return [l[0]*2] + dil(l[1:])
# print(su(3))
# l = [i for i in range(10)]
# print(dil(l))

# n=int(input())
# ans=[]

# def dfs(i,c,d):
# 	if i==n:
# 		ans.append(c)
# 		return
# 	for j in range(0,d+1):
# 		dfs(i+1,c+chr(97+j),d+(j==d))

# dfs(0,"",0)

# print("\n".join(ans))

"""
DFSを実装する.再帰を計算する必要があるので，関数の定義が必要
a - a -a
      -b
  - b -a
      -b
      -c
"""
n = int(input())

def dfs(s,mx):
    if len(s)==n:
        print(s)
        return None
    for i in range(ord('a'),mx+1+1):
        dfs(s+chr(i),max(mx,i))
dfs('',ord('a')-1)