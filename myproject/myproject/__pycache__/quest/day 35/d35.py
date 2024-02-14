#                         #PACK
# import tkinter as tk
# root=tk.Tk()

# # test=tk.Label(root,text='Chevala',bg='red',fg='white')
# # test.pack(side=tk.RIGHT)

# # test=tk.Label(root,text='Pacha',bg='green',fg='white')
# # test.pack(side=tk.RIGHT)

# # test=tk.Label(root,text='Neela',bg='Blue',fg='white')
# # test.pack(side=tk.RIGHT)

#                 #padding

# test=tk.Label(root,text='Red',bg='red',fg='white')
# test.pack(padx=10,pady=100,side=tk.LEFT)




# root.mainloop()

                #geometry and place

import tkinter as tk
root=tk.Tk()

root.geometry('250x250+575+200')

# test=tk.Label(root,text='Red',bg='red',fg='white')
# test.place(x=30,y=10)

# test=tk.Label(root,text='Blue',bg='Blue',fg='white')
# test.pack(padx=10,pady=100,side=tk.LEFT)

tk.Label(root,text="abc",bg='red',fg="white").place(x=10,y=10)








root.mainloop()