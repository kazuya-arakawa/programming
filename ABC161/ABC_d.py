k = int(input())

# TLEになる
# cnt = 9
# if k < 10:
#     print(k)
# else:
#     for i in range(10,10**16+2):
#         s = str(i)
#         flag = True
#         for j in range(len(s)-1):
#             if abs(int(s[j])-int(s[j+1])) > 1:
#                 flag = False
#                 break
#         if flag == True:
#             cnt += 1
#         if cnt == k:
#             print(i)
#             break
l = [i for i in range(1,10)]
for i in range(k):
    if l[i]%10 != 0:
        l.append(10*l[i]+l[i]%10-1)
    l.append(10*l[i]+l[i]%10)
    if l[i]%10 != 9:
        l.append(10*l[i]+l[i]%10+1)
print(l[k-1])