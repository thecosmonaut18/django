                #using question mark ?

# import re
# w="pillows heo my are kite wells helo"
# y=re.findall("he.?o",w)
# print(y)

# import re
# x="hello my name is John. I have two cats Mia and Mac"
# y=re.findall(r"\b\w{3}\b",x)
# print(y)

# import re


# text=" Imp dates : 2022-01-01,2023-05-15 and 2023-12-31"
# y=re.findall(r"\d{4}-\d{2}-\d{2}",text)
# print(y)

# a="The THE the ThE"
# b=re.findall('the',a,re.IGNORECASE)
# print(b)

# text="there are 123 apples and 456 bananas"
# x=re.findall("\d{3}",text)
# print(x)

# text="Hello world! This is a sample text"
# words=re.split(r"\s",text)
# print(words)

# n=(1,2,3,4,5)
# l=len(n)

# for i in range(l):
#     for j in range(l):
#         if i==j or i+j==l-1:
#             print(n[j],end=" ")

#         else:
#             print(" ",end=" ")
        
#     print()

# n=(1,2,3,4,5)
# l=len(n)

# for i in range(l):
#     for j in range(l):
#         if i==j or i+j==l-1:
#             print(n[i],end=" ")

#         else:
#             print(" ",end=" ")
        
#     print()


            # heart pattern
# n = 4

# # upper part of the heart
# for i in range(n//2, n, 2):
#     # print first spaces
#     for j in range(1, n-i, 2):
#         print(" ", end=" ")
#     # print first number
#     for j in range(i):
#         print(j+1, end=" ")
#     # print second spaces
#     for j in range(1, n-i+1, 1):
#         print(" ", end=" ")
#     # print second number
#     for j in range(i):
#         print(j+1, end=" ")
#     print()

# # lower part
# for i in range(n, 0, -1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i*2):
#         print(j+1, end=" ")
#     print()


                #spy numbers

# n=int(input("Enter the number : "))
# temp=n
# sum=0
# prd=1

# while temp>0:
#     lastdigit=temp%10
#     sum=sum+lastdigit
#     prd=prd*lastdigit
#     temp=temp//10

# if sum==prd:
#     print("Spy Number")
# else:
#     print("Not spy number")


            #spearl number

# n=int(input("Enter the number : "))
# temp=n
# sum=0
# prd=1

# while temp>0:
#     lastdigit=temp%10
#     sum=sum+lastdigit
#     prd=prd*lastdigit
#     temp=temp//10
  
# add=sum+prd

# if n==add:
#     print("Spearl number")
# else:
#     print("Not spearl number")

                #automorphic number

# n=int(input("Enter the number : "))
# temp=n
# sqr=n**2
# while temp>=0:
#     d=n%10
#     s=sqr%10