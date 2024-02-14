                                ####            PYTHON SET          ####


# set={1,2,3}
# print(set)
# print(type(set))


# s={}
# print(type(s))


# a=set()
# print(a)
# print(type(a))


                    #list to set

# a=[1,2,3,4,4,6,5,9,8]
# print(a)
# b=set(a)
# print(b)

                    #update
# a={11,22,33}
# print(a)
# a.update(["hi",'hello'])
# print(a)

# a={11,22,33}
# print(a)
# a.update("hi")
# print(a)

# a={11,22,33}
# print(a)
# a.add("hii")            #single elememts
# print(a)

# a={1,2,3,4,5}
# for i in a:
#     print(i)

                    #remove
# a={11,22,33}
# a.discard(11)
# print(a)

# a={11,22,33}
# a.remove(11)
# print(a)
#                 #errors
# a={11,22,33}
# a.discard(66)
# print(a)            #no error

# a={11,22,33}
# a.remove(111)
# print(a)            #error



                #MATHEMATICAL OPERATIONS
            #union

# a={1,2,3,4}
# b={3,4,5,6,7}
# print(a|b)

            #intersection

# a={1,2,3,4}
# b={3,4,5,6,7}
# print(a&b)

#             #difference

# a={1,2,3,4}
# b={3,4,5,6,7}
# print(a-b)

#             #symmetric diff

# a={1,2,3,4}
# b={3,4,5,6,7}
# print(a^b)

# my_set=set("apple")
# print('a' in my_set)


# a={1,2,3,4}
# b={3,4,5,6,7}

# # a|=b
# # a&=b
# # a-=b
# a^=b
# print(a)


# a={1,2,3,4,5,6,7,8,9}
# b={3,4,5,6,7}

# print(a.isdisjoint(b))
# print(a.issuperset(b))
# print(a.issubset(b))
# print(b.issubset(a))


# studentlist=['aishu','sneha','ann mary','betson','swathi','jilson','jibin','alson','sona','neha']
# placedstudents=['jilson','swathi','aishu','sneha','ann mary']

# notplacedstudents=set(studentlist)-set(placedstudents)
# print("Students yet to be placed : ",notplacedstudents)


# attackers=['Messi','Ronaldo','Foden','Mbappe','Haaland','Neymar']
# defenders=['Stones','Pique','Ramos','Ottamendi','Walker']

# footballers=set(attackers)|set(defenders)
# print("Footballers : ",)
# for i in footballers:
#     print(i)


wipro=['Jilson','Swathi',"Aiswarya",'Sneha','Ann mary']
tcs=['Jilson','Swathi','Alson']
infosys=['Jilson','Swathi','Betson','Ann mary']

placedstudents=set(wipro)&set(tcs)&set(infosys)
print("Placed students are ",placedstudents)