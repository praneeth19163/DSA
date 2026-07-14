n=int(input("enter no of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print((i+j+1)%2,end=' ')
    print()