k = int(input())

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
cnt = 9
if k < 10:
    print(k)
else:
    while(True):
        s = str(k)
        if abs(int(s[:-2])-int(s[:-1])) > 1:
            k += 10
        else