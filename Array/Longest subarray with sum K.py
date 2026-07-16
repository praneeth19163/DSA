# #brute force
# a=[1,1,2,3,1,1,1,1,3,2,5,8,15]
# k=100
# sum=0
# tc=0
# lc=0
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         if sum < k:
#             sum+=a[j]
#             tc+=1
#             if sum == k:
#                 if lc<tc:
#                     lc=tc
#                 sum=0
#                 tc=0
#                 print(a[i:j+1])
#                 break
#         if sum > k:
#             sum=0
#             tc=0
#             break
# print(lc)
# #tc is o(n^2)


#optimal solution:
