                #armstrong
# num=int(input("Enter a number="))
# sum=0
# n=num
# a=0
# while n>0:
#     a=n%10
#     sum=sum+a**3
#     n//=10
# if num==sum:
#     print("armstrong")
# else:
#     print("not armstrong")

                #palindrome
num=int(input("Enter a number="))
rev=0
n=num
while n>0:
    a=n%10
    rev=rev*10+a
    n//=10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")