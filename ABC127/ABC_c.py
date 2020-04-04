import numpy as np
N,M = map(int,input().split())
LR = [list(map(int,input().split())) for i in range(M)]
LR = np.array(LR)

maxi = 10**6
mini = 0
for lr in LR:
    mini = max(lr[0],mini)
    maxi = min(lr[1],maxi)
if maxi-mini < 0:
    print(0)
else:
    print(maxi-mini+1)