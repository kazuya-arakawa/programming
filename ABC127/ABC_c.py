import numpy as np
N,M = map(int,input().split())
LR = [list(map(int,input().split())) for i in range(M)]
LR = np.array(LR)

mini = max(LR[:,0])
maxi = min(LR[:,1])

if maxi-mini < 0:
    print(0)
else:
    print(maxi-mini+1)