n=int(input("enter no of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(65+n-j-1),end='')
    print()