# a=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
# b=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
# c=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
# num=int(input("Enter a number between (0 and 999) = "))
# if num<10:
#     print(a[num])
# elif num>=10 and num<20:
#     print(b[num-10])
# elif num>19 and num<100:
#     m=num%10
#     f=num//10
#     if m==0:
#         print(c[f])
#     else:
#         print(c[f]+" "+a[m])
# elif num>99 and num<1000:
#     ones=num%10
#     temp=num%100
#     num=num//10
#     tens=num%10
#     hund=num//10
#     if tens==0 and ones==0:
#         print(a[hund]+" hundred")
#     elif tens==0:
#         print(a[hund]+" hundred and "+a[ones])
#     elif temp>9 and temp<20:
#         print(a[hund]+" hundred and "+b[temp-10])
#     elif ones==0:
#         print(a[hund]+" hundred and "+c[tens])
#     else:
#         print(a[hund]+" hundred and "+c[tens]+" "+a[ones])
# else:
#     print("Number exeeds the limit")
    


num=int(input("Input dogs age in human years "))
first=10.5
second=10.5
if num==1:
    print("The dogs age in dogs year is ",first)
elif num==2:
    print("The dogs age in dogs year is ",first+second)
elif num>2:
    print("The dogs age in dogs year is ",((num-2)*4)+first+second)
else:
    print("Wrong input")