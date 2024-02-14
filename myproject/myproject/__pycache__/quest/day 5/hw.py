# n=5
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

# n=5
# a=0
# for i in range(n,0,-1):
#     a+=1
#     for j in range (1,i+1):
#         print(a,end=" ")
#     print()

# n=5
# a=n
# for i in range(n,0,-1):
#     for j in range (1,i+1):
#         print(a,end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range (0,i+1):
#         print(j,end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range (1,i+1):
#         print(n,end=" ")
#     print()

# rows = 5
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i * 2 - 1), end=" ")
#         j = j + 1
#     i = i+1
#     print()

rows=5

number = 1
for i in range(1,rows,1):
    for j in range(1,rows):
        print(number, end=" ")
        j=j+1
        number += 2
    print()
