a='HIII'
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.title())


# print(a.islower())
# print(a.isalpha())
# print(a.isdigit())
# print(a.isalnum())




# a={'name':'anu','age':7,'email':'anu@gmail.com'}
# b=a.pop('name')
# # print(a)
# # print(b)
# a['First_name']=b
# print(a)




# a={'name':'jilson','age':21,'email':'jilson@gm','place':'ekm'}
# print(a)
# n=input("Enter the key to be changed : ")
# z=input("Enter the Key : ")
# if n in a:
#     b=a.pop(n)
#     a[z]=b
#     print(a)
# else:
#     print("Key not found")



# z={}
# n=int(input("Enter number of Values : "))
# for i in range(n):
#     k=input("enter the key value : ")
#     v=(input("enter the values : "))
#     z[k]=v
# print(z)
# p=input("Enter the key to be changed : ")
# q=input("Enter the Key : ")
# if p in z:
#     b=z.pop(p)
#     z[q]=b
#     print(z)
# else:
#     print("Key not found") 


# i=1
# while i:
#     val=int(input("Enter the value : "))
#     while val<=5:
#         if val==1:
        
#             print("add")
#             break
#         elif val==2:
#             print("view")
#             break
#         elif val==3:
#             print("update")
#             break
#         elif val==4:
#             print("delete")
#             break
#         elif val==5:
#             print("Exit")
#             i=0
#             break
#     else:
#         print("Invalid choice")


print("1 -> add to contacts")
print("2 -> view contacts")
print("3 -> delete contact")
print("4 -> update contact")
print("5 -> Exit")
i=1
p={}
while i:
    val=int(input("Enter the value : "))
    while val<=5:
        if val==1:
            z={}
            k=input("Enter the name : ")
            v=(input("Enter the phone number : "))
            e=(input("Enter the email : "))
            z['name']=k
            z['phn']=v
            z['email']=e
            p[k]=z
            print("Added Successfully")
            break
        elif val==2:
            n=int(input("Do you want to print whole contact list? (if yes press 1/ if not press 0)  : "))
            if n==1:
                print(p)
            elif n==0:
                name=input("Enter the name : ")
                print(p[name])
            break
        elif val==3:
            dname=input("Enter the name : ")
            del p[dname]
            print("Deleted")
            print(p)
            break
        elif val==4:
            uname=input("Enter the name to be updated : ")
            if uname in p:
                update=int(input("What should be Updated  1 -> name, 2 -> email, 3 -> phone number : "))
                if update==1:
                    up=p[uname]
                    newname=input("Enter New Name : ")
                    up['name']=newname
                    nn=p.pop(uname)
                    p[newname]=nn
                elif update==2:
                    up=p[uname]
                    newemail=input("Enter new email : ")
                    up['email']=newemail
                elif update==3:
                    up=p[uname]
                    newphn=input("Enter new phone number : ")
                    up['phn']=newphn
                break
            else:
                print("Wrong input")
            
            
        elif val==5:
            print("Exit")
            i=0
            break
    else:
        print("Invalid choice")