                        #multiplication table of a number
# num=int(input("Enter a number= "))
# a=1
# mul=1
# while a<=10:
#     mul=a*num
#     print(a,"*",num,"=",mul)
#     a+=1

                        #number of digits in a number
# num=int(input("Enter a number="))
# a=0
# while num>0:
#     # num%10
#     num=num//10
#     a+=1
# print(a)

                        #sum of digits
# num=int(input("Enter a number="))
# a=0
# sum=0
# while num>0:
#     a=num%10
#     sum+=a
#     num//=10
# print("Sum",sum) 

                        # reverse of a number in python
# num=int(input("Enter a number="))
# rev=0
# a=0
# while num>0:
#     a=num%10
#     rev=rev*10+a
#     num//=10
# print("Reverse=",rev)
                        #fibbonacci series
num=int(input("No of terms= "))
first=0
second=1
a=0
while a<num:
    print(first)
    third=first+second
    first=second
    second=third
    a+=1
                        # sum of digits
# num=int(input("Enter a number="))
# sum=0
# while num>0:
#     sum+=num
#     num-=1
# print("Sum=",sum)