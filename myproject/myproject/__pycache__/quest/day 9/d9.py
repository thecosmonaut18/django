                    #pop
# cosmonaut=["c","d","f","y","o"]
# print(cosmonaut)
# c=cosmonaut.pop()
# print(cosmonaut)
# print(c)

# cosmonaut=["c","d","f","y","o"]
# print(cosmonaut)
# c=cosmonaut.pop(2)
# print(cosmonaut)
# print(c)

                    #del
# cosmonaut=["c","d","f","y","o","8","u"]
# print(cosmonaut)
# del cosmonaut[3]
# print(cosmonaut) 


# cosmonaut=["c","d","f","y","o","8","u"]
# print(cosmonaut)
# del cosmonaut[1:3]
# print(cosmonaut)        #delete first value and continue with next value

                    #clear
# cosmonaut=["c","d","f","y","o","8","u"]
# cosmonaut.clear()
# print(cosmonaut)          #clear the complete list and return null list

                    #remove
# cosmonaut=["c","d","f","y","o","8","u"]
# print(cosmonaut)
# cosmonaut.remove("c")
# print(cosmonaut)

                    #to replace with null value
# cosmonaut=["c","d","f","y","o","8","u"]
# cosmonaut[2]=""
# print(cosmonaut)

# list1=["M","na","i","Ke"]
# list2=["y","me","s","lly"]
# list3=[]
# # print(list1)
# # print(list2)
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])
# print(list3)


l1=["M","na","i","Ke","k"]
l2=["y","me","s","lly"]
l3=[]
la=len(l1)
lb=len(l2)
if la<lb:
    l=lb
else:
    l=la
for i in range(l):
    c=''
    if i<la:
        c+=l1[i]
    if i<lb:
        c+=l2[i]
    l3.append(c)
print(l3)