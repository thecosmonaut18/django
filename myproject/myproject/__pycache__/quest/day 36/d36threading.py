#             #THREADING

# import threading
# import time
# a=[1,2,3,4]
# def cube(a):
#     for i in a:
#         print("Cube = ", i**3)
#         # print(threading.current_thread())
#         time.sleep(1)
# def square(a):
#     for i in a:
#         print("Square = ",i**2)
#         print(threading.current_thread())
#         time.sleep(1)

# # square()
# # cube()

# t=threading.Thread(target=cube,args=(a,))
# t2=threading.Thread(target=square,args=(a,))

# t.start()
# t2.start()
# t.setName("Cube thread")
# t2.setName("Square thread")
# print(threading.enumerate())


from threading import Thread
import time

class MyThread(Thread):
    def cube(self,b):
        for i in b:
            print("-------",i)
            print("cube = ",i**3)
            time.sleep(1)

    def run(self):
        a=(1,2,3,4)
        self.cube(a)

class MyThread2(Thread):
    def square(self,b):
        for i in b:
            print("-------",i)
            print("square = ",i**2)
            time.sleep(1)

    def run(self):
        a=(1,2,3,4)
        self.square(a)

t1=MyThread()
t1.start()

t2=MyThread2()
t2.start()