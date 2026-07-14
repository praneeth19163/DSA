n=int(input("enter no of rows:"))

for i in range((2*n)-1):
    for j in range((2*n)-1):
        top=i
        bottom=((2*n)-1-i-1)
        left=j
        right=((2*n)-1-j-1)
        print(n-(min(top,bottom,left,right)),end='')
    print()
