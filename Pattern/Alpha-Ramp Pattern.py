# n=int(input("enter the no of rows:"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(chr(65+i),end='')
#     print()
n=int(input("enter the no of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        a=65+n+j-i-1
    
        print(chr(a),end='')
    print()
