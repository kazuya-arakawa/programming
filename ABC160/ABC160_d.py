# import numpy as np
# from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# # n = int(input())
# n,x,y = map(int,input().split())
# # A = list(map(int,input().split()))
# # An = [list(map(int,input().split())) for i in range(n)]
# l = np.zeros((n,n))
# l[0][1] = 1
# l[n-1][n-2] = 1
# l[x-1][y-1] = 1
# l[y-1][x-1] = 1
# for i in range(n-3):
#     l[i+1][i] = 1
#     l[i+1][i+2] = 1

# l = shortest_path(l)
# print(l)
# for j in range(1,n):
#     print(np.count_nonzero(l==j))
N,X,Y=map(int,input().split())
ans=[0]*(N-1)
for i in range(1,N):
	for j in range(i+1,N+1):
		a=min(j-i,abs(i-X)+abs(Y-j)+1)
		ans[a-1]+=1
for i in range(N-1):
	print(ans[i])