# #brute force
# a=[1,2,3,5]
# n=5
# for i in range(1,n):
#     for j in range(len(a)):
#         if i == a[j]:
#             break
#     else:
#         print(i)
#         break
#tc is o(n^2)

# #better approach(hashing)
# a=[1,2,3,5,6,4]
# n=7
# b=[0]*(n+1)
# for i in a:
#     b[i]=1
# for i in range(1,len(b)):
#     if b[i] == 0:
#         print(i)
#         break
# # tc=o(n)+o(n) and sc is o(n)



#optimal approach
#the sum of frst n natural numbers formula we are using and we can also use xor concept but we can use it later in bitwise
a=[1,2,3,5]
n=5
sum_of_array=0
import math
sum_of_n=math.ceil(n*(n+1)/2)
for i in a:
    sum_of_array+=i
missing_number=sum_of_n - sum_of_array
print(missing_number)

