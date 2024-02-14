
#                 #THREAD SYNCRONIzATION

# import threading
# x = 0
# # lock
# def increment(lock):
#     global x
    
#     for i in range(10000000):
#         lock.acquire()
#         x+=1
#         # print(x)
#         # print(x, threading.currentThread())
#         lock.release()  
          
      
          
# def main_task():
#     global x
#     x = 0
#     lock = threading.Lock()
#     # t1 = threading.Thread(target=increment)
#     # t2 = threading.Thread(target=increment)
#     # t2.setName('T2')
#     t1 = threading.Thread(target=increment,args=(lock,))
#     t2 = threading.Thread(target=increment,args=(lock,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
    
# for i in range(10): 
#     main_task()        
#     print("Iteration {0}: x = {1}".format(i,x)) 





# import threading
# x=0
# def increment(lock):
#     global x
#     for i in range(100000):
#         lock.acquire()
#         x+=1
#         # print(x)
#         lock.release()


# def maintask():
#     global x
#     x=0
#     lock=threading.Lock()
#     # t1 = threading.Thread(target=increment)
#     # t2 = threading.Thread(target=increment)
#     t1 = threading.Thread(target=increment,args=(lock,))
#     t2 = threading.Thread(target=increment,args=(lock,))
    
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# for i in range(10): 
#     maintask()        
#     print("Iteration {0}: x = {1}".format(i,x)) 

# increment()
# maintask()
# print("-------------------------------------------------------------------------------------------------------------")
# maintask()


            #REGULAR EXPRESSION

# import re


# txt="The rain in Spain"
# x=re.findall("ai",txt)
# print(x)

# txt="The rain in Spain"
# x=re.search("ai",txt)
# # print(x)
# print('''first char in''',x.start())
# print('''last char in''',x.end())

# txt="The rain in Spain"
# x=re.findall("[a-m]",txt)
# print(x)

# txt="The3 ra1in 1in 5Spain"
# x=re.findall("[12345]",txt)
# print(x)

# txt="b The rain in Spain"
# x=re.findall("^b",txt)
# print(x)

# txt="The b rain in Spain"
# x=re.findall("^b",txt)
# print(x)          #if in bw it wont work


# txt="The rain in Spain"
# x=re.findall("[^arn]",txt)
# print(x)

# txt="The rain in Spain"
# # x=re.sub("\s",'9',txt)
# # x=re.sub("\s",'9',txt,1)
# x=re.sub("\s",'9',txt,7)
# print(x)