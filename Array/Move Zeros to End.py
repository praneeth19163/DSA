a=[1,0,2,3,0,0,4,5,1]
c=0
for i in range(0,len(a)):
    a[i-c]=a[i]
    if a[i]==0:
        c+=1
for i in range(c):
    a[len(a)-1-i]=0
print(a)


#  #Two pointer approach
# j=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[i],nums[j]=nums[j],nums[i]
#         j+=1
    