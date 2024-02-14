# a=[]
# for i in "get":
#     for j in "set":
#         # print(i+j)
#         a.append(i+j)
# print(a)

# c=[a+b for a in "get" for b in "set"]
# print(c)

# a=[1,2,3,4,5,6,7,8,9,10]
# print(a)
# # even=[e for e in a if e%2==0]
# # print(even)

# n=["e" if i%2==0 else "o" for i in a]
# print(n)


# six=[i for i in range(100) if i//10==6 or i%10==6]
# six=[i for i in range(100) if "6" in str(i)]
# print(six)



# a="hi my name is Jilson I am from Kochi"
# b=a.split()
# # print(b)
# fiveletter=[i for i in b if len(i)<5]
# print(fiveletter)


# a="abcdefghijklmnopqrstuvwxyz"
# vow=[i for i in a if i not in "aeiou"]
# # print(vow)
# # p=str(vow)
# # print(type(p))
# # print(p)
# b="".join(vow)
# print(b)


# li=[1,2,4,6,8,3,5,7,56,9]
# final_list=list(filter(lambda x: (x%2!=0),li))
# print(final_list)

# final_list=list(map(lambda x: x*2,li))
# print(final_list)


# from functools import reduce
# li=[5,2,4,8,29,20]
# sum=reduce((lambda x,y:x+y),li)
# print(sum)