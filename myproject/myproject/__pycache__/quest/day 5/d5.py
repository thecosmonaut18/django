                        #even num in limit
# n=int(input("Enter a starting number="))
# m=int(input("Enter the limit number="))
# for i in range(n,m):
#     if i%2==0:
#         print(i)

                        #fibonacci series in a limit
# num=int(input("Enter the limit number="))
# first=0
# second=1

# for i in range(0,num,1):
#     if i>num:
#         print(first)
#         third=first+second
#         first=second
#         second=third
#     else:
#         print(first)

                        # pattern
# n=5
# for i in range(1,n+1):
#     for j in range (i):
#         print(i,end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# num=int(input("Enter the limit number="))
# first=0
# second=1

# for i in range(0,num,1):
#     third=first+second
#     first=second
#     second=third
#     print(first)
#     if first<num:  
#         print(first)
#         break
    
# num=int(input("Enter the limit number="))
# first=0
# second=1
# a=0
# while a<num:
#     if a<num:
#         print(first)
#         third=first+second
#         first=second
#         second=third
#         a+=1
#     else:
#         break

# def fibonacci_series(limit):
#     series = [0, 1]  # Initialize the series with the first two Fibonacci numbers
#     while series[-1] < limit:
#         next_num = series[-1] + series[-2]
#         if next_num < limit:
#             series.append(next_num)
#         else:
#             break
#     return series

# # Example usage
# limit = 100  # Specify the limit here
# fib_series = fibonacci_series(limit)
# print(fib_series)
