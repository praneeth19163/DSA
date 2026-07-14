n=int(input("enter no of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end='')
    for j in range(0,((2*n)-(2*(i+1)))):
        print(" ",end='')
    for j in range(i+1,0,-1):
        print(j,end='')
    print()