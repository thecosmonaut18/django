#                 #q no 38
# n=int(input("Enter no of rows and columns : "))
# a=[]
# z=[]
# for i in range(n):
#     b=[]
#     for j in range(n):
#         e=int(input("Enter the elements of metrix 1 = "))
#         b.insert(j,e)
#     a.insert(i,b)
# print(a)
# for i in range(n):
    
#     d=[]
#     for j in range(n):
#         e=int(input("Enter the elements of metrix 2 = "))
#         d.insert(j,e)
#     z.insert(i,d)
# print(z)
# sum=[]
# for i in range(n):
#     temp=[]
#     for j in range(n):
#         t=a[i][j]+z[i][j]
#         temp.append(t)
#     sum.append(temp)
# print("SUM = ",sum)

                #to remove duplicates in a list
# a=[1,2,3,4,5,6,1]
# print(a)
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# a=int(input("Enter the num of values = "))
# b=[]
# for i in range(a):
#     e=int(input("Enter the elements = "))
#     b.append(e)
# print(b)
# c=[]
# for i in b:
#     if i not in c:
#         c.append(i)
# print(c)

                #to remove duplicates in a sublist

# a=[[1,2,3,1],[7,3,5,7,5]]
# print(a)
# b=[]
# for i in a:
#     temp=[]
#     for j in i:
#         if j not in temp:
#             temp.append(int(j))
#     b.append(temp)
# print(b)

                #to get the removed duplicates
# a=[1,2,3,4,5,6,1]
# print(a)
# b=[]
# c=[]
# for i in a:
#     if i not in b:
#         # b.append(i)
#         # print(b)
#         pass
#     else:
#         c.append(i)
# print(c)

# a=[1,2,3]
# if len(a)==0:
#     print("Empty")
# else:
#     print("Not empty")

# a=[]
# if a:
#     print("list")
# else:
#     print("empty")


# if False:
#     print("Yes")
# else:
#     print("no")


# i=1
# while i:
#     a=int(input("Enter 1st val = "))
#     b=int(input("Enter 2nd val = "))
#     if a==0 and b==0:
#         # break
#         i=0
#     sum=a+b
#     print("sum =",sum)


# a=list("hello")
# print(a)

# a=[1,2,3]
# s=str(a)
# print(s)