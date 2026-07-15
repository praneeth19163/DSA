a = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1,1,1,1]
max_count=0
temp_count=0
for i in range(len(a)):
    if a[i]==1:
        temp_count+=1
    if a[i]==0 :
        if max_count < temp_count:
            max_count=temp_count
        temp_count=0
if max_count < temp_count:
    max_count = temp_count
print(max_count)
    