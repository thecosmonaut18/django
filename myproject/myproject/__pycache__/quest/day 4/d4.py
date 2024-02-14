                    # for loop
for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(1,4,-1):
    print(i)        #no output

for i in range(5,1,-1):
    print(i)

                        #sum of 10 numbers
# sum=0
# for i in range(1,11,1):
#     sum+=i
# print(sum)

                        #prime number

# num=int(input("Enter a number="))
# for i in range(2,num):
#     if num%i==0:
#         print("it is not prime")
#         break
# else:
#     print("prime")

                        #prime with limit
num=int(input("Enter starting number="))
lim=int(input("Enter a limit="))

for i in range(num,lim):
    for n in range(2,i):
        if i%n==0:
            break
    else:
        print(i)


