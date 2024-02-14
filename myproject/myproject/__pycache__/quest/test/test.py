# # p=0
# q=(int(input("Enter the Starting value : ")))
# r=(int(input("Enter the ending value : ")))

# for i in range(q,r):
#     for j in range(2,i):
#         if i%j==0:
#             # print(j)
#             # print(i)
#             break
#     else:
#         print(i)
#         # break



# n=int(input("Enter the digit : "))
# a=0
# m=1
# while n>0:
#     n=n//10
#     a+=1
#     m=m*a
# print(a)
# print(m)




# a=[1,2,3,4,5,6,7,8,9]
# b=[]
# sum=0
# for i in a:
#     if i%2!=0:
#         b.append(i)
# print(b)
# for i in b:
#     sum+=i
# print(sum)


n=int(input("Enter the number of elements : "))
a=[]
for i in range(n):
    b=int(input("Enter the elements : "))
    a.append(b)
print(a)
sum=0
c=[]
for i in a:
    
    if i%2!=0:
        c.append(i)
print(c)
for i in c:
    sum=sum+i
print(sum)