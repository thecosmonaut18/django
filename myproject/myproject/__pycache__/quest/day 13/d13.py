                    #DICTIONARY

# a={'name':'Jilson','age':21,'place':'kochi'}
# print(a['name'])
# print(a['age'])
# a['DOB']='18 dec'
# print(a)

# for i in a.values():
#     print(i)

# for i in a.items():
#     print(i)

# b=a.pop('name')
# print(a)
# print(b)

# b=a.popitem()
# print(a)
# print(b)



# name1=input("Enter the Name : ")
# email1=input("Enter email : ")
# phn1=input("Enter phone number : ")
# a={}
# a['name']=name1
# a['email']=email1
# a['phn']=phn1
# print(a)


# a={}
# for i in range(1,11):
#     a[i]=i*i
# print(a)

# a={}
# k=['name','email','phn','place']
# v=['anu','anu@gm',7736,'ekm']

# for i in range(4):
#     a[k[i]]=v[i]
# print(a)


# prices={'Apple':1.99,'Cantaloupe':3.99,'Banana':2.00,'Orange':1.69,'Grapes':3.14}
# # print(prices)
# # print(sorted(prices))
# # print(sorted(prices.keys()))
# print(sorted(prices.values()))
# print(sorted(prices.items()))
# print(sorted(prices.values(),reverse=True))

# z={}
# n=int(input("Enter number of Values : "))
# for i in range(n):
#     k=input("enter the key value : ")
#     v=int(input("enter the values : "))
#     z[k]=v
# print(z)
# s=0
# for i in z:
#     s+=z[i]
# print(s)




# z={}
# n=int(input("Enter number of Values : "))
# for i in range(n):
#     k=input("enter the key value : ")
#     v=input("enter the values : ")
#     z[k]=v
# print(z)
# print(sorted(z.values()))


# z={}
# n=int(input("Enter number of Values : "))
# for i in range(n):
#     k=input("enter the key value : ")
#     v=input("enter the values : ")
#     z[k]=v
# print(z)
# print(sorted(z.values(),reverse=True))



# z={}
# n=int(input("Enter number of Values : "))
# for i in range(n):
#     k=input("enter the key value : ")
#     v=int(input("enter the values : "))
#     z[k]=v
# print(z)
# print(sum(z.values()))


a={'a':1,'b':2,'c':6}
print(min(a.values()))
print(max(a.values()))


z={}
n=int(input("Enter number of Values : "))
for i in range(n):
    k=input("enter the key value : ")
    v=int(input("enter the values : "))
    z[k]=v
print(z)
print(min(z.values()))
print(max(z.values()))


# a={'name':'anu','age':7,'email':'anu@gmail.com'}
# b=a.pop('name')
# # print(a)
# # print(b)
# a['First_name']=b
# print(a)
