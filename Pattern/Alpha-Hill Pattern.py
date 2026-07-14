n=int(input("enter no of rows:"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    for j in range(0,i+1):
        print(chr(65+j),end='')
    for j in range(0,i):
        print(chr(65+i-j-1),end='')
    print()