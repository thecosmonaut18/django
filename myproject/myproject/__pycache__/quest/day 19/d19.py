# f=open('cos.txt','w')
# f.write('Hello world')
# f.write("\n")
# f.write('Hello world 1')  #it rewrites the file
# f.write("\n")
# f.write('hello world 2')
# # f.close()
# f=open('cos.txt','r')
# # print(f.read())
# for i in f:
# #     print(i)
# f=open('file.txt','a')
# f.write("\n")
# f.write('Hey world')

# with open('cos.txt','w') as f:
#     f.write('Hello Hello')

# f=open('jils.txt','r')
# print(f.readline())
# with open('jils.txt','r') as k:
#     d=k.readline()
#     # print(d)
#     for i in d:
#         print(i)

# f=open('jils.txt','w')

def story():
    s=0
    r=open('jils.txt','r')
    d=r.readlines()
    for i in d:
        if i[0]=='T':
            s+=1
    print(s)


story()
        



    # print(d[1:3])
    # for i in d:
    #     a=i.split('\n')
    #     for j in a:
    #         print(j)

