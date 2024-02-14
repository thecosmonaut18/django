# import random
# a=random.randint(1,5)
# print(a)

# from random import randint
# a=randint(1,5)
# print(a)

# from random import randint as c
# a=c(1,5)
# print(a)


# import random
# a=random.randint(1,5)
# print('nnnnnnnnnnn',a)
# chs=3
# while chs>0:
#     n=int(input("Guess the number from 1 to 5 = "))
#     if n==a:
#         # print("Your guess is correct")
#         print("Winner Winner Chicken Dinner")
#         break
#     else:
#         print("Your guess is wrogn")
#     chs-=1
# else:
#     print("Game over")


import random
def d():
    a=random.randint(1,10)
    return a
def guess():
    n=d()
    chs=3
    win=0
    while chs>0:
        p=int(input("Guess the number from 1 to 10 : "))
        if p==n:
            win=1
            break
        else:
            print("Your guess is wrogn")
            
        chs-=1


    if win==1:
        return True
    else:
        return False


s=guess()

if s==True:
    print("con")
else:
    print('los')




