n=int(input("enter no of rows:"))
for i in range(0,n):
    c=65
    for j in range(0,i+1):
        print(chr(c),end=' ')
        c+=1
    print()

# n = int(input("Enter number of rows: "))

# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")
#     print()