# from tkinter import *

# root = Tk()
# root.mainloop()

# from tkinter import *

# shabna = Tk()
# shabna.title("welcome to python lobby")
# lbl = Label(shabna, text = "we are python lobby.ian",font=("cambria",12),fg="white",bg="black")
# lbl.pack()

# shabna.mainloop()

#   from tkinter import *

#   shabna = Tk()
#   shabna.title("hello how are you")
#   lbl = Label(shabna, text = " hi, am shabna",font=("cambria",12),fg="white",bg="black")
#   lbl.pack()
#   def clicked():
#      print(" i am clicked")
#   btn = Button(shabna, text="click me",command=clicked)
#   btn.pack()
#   entry

#   shabna.mainloop()

# from tkinter import *

# shabna = Tk()
# shabna.title("hello how are you")
# lbl = Label(shabna, text = " hi, am shabna",font=("cambria",12),fg="white",bg="black")
# lbl.pack()
# def clicked():
#     print(" i am clicked")
# btn = Button(shabna, text="click me",command=clicked)
# btn.pack()
# entry = Entry(shabna,bg="yellow",fg="red",bd=5)
# entry.place(x=100,y=100)

# shabna.mainloop()

from tkinter import *

shabna = Tk()
shabna.title("hello how are you")
lbl1 = Label(shabna, text = "facebook",font=("klavika",30),fg="white",bg="blue")
lbl1.place(x=580,y=100)
lbl2 =Label(shabna,text="enter your username",font=("klavika",10),fg="black",bg="white")
lbl2.place(x=600,y=160)
entry1= Entry(shabna,bg="white",fg="black",bd=5)
entry1.place(x=600,y=190)
lbl3 =Label(shabna,text="enter your password",font=("klavika",10),fg="black",bg="white")
lbl3.place(x=600,y=220)
entry2=Entry(shabna,bg="white",fg="black",bd=5)
entry2.place(x=600,y=250)
def clicked():
    print(" i am clicked")
btn = Button(shabna, text="login",font=("klavika",10),fg="white",bg="blue",command=clicked)
btn.place(x=640,y=280)


shabna.mainloop()
