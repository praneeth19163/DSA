n=int(input("enter no of rows"))
for i in range(0,n):
    c=65
    for j in range(n-i,0,-1):
        print(chr(c),end='')
        c=c+1
    print()