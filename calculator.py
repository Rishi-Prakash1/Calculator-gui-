from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("400x300")
window.title("Calculator")
#------------------------------------------------------


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
def cleardisplay():
    global operator
    operator = " "
    text_input.set(" ")
def Equal():
    global operator
    res = str(eval(operator))
    text_input.set(res)
    operator = " "
#-------------------------------------------------------

text_input= StringVar()
operator=" "
  
e1 = Entry(width=27, font=8,borderwidth=3, textvariable=text_input).place(x=40,y=10)
b1 = Button(text="  1  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(1)).place(x=40,y=60)
b2 = Button(text="  2  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(2)).place(x=115,y=60)
b3 = Button(text="  3  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(3)).place(x=190,y=60)
devide = Button(text="  /  ",font=10,width=6,bg="blue",relief=SOLID,command=lambda:btnclick("/")).place(x=265,y=60)

b4 = Button(text="  4  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(4)).place(x=40,y=105)
b5 = Button(text="  5  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(5)).place(x=115,y=105)
b6 = Button(text="  6  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(6)).place(x=190,y=105)
multiply = Button(text="  x  ",font=10,width=6,bg="blue", relief=SOLID,command=lambda:btnclick("*")).place(x=265,y=105)

b7 = Button(text="  7  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(7)).place(x=40,y=150)
b8 = Button(text="  8  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(8)).place(x=115,y=150)
b9 = Button(text="  9  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(9)).place(x=190,y=150)
subtract = Button(text="  -  ",font=10,width=6,bg="blue",relief=SOLID,command=lambda:btnclick("-")).place(x=265,y=150)

clr = Button(text=" clr ",font=10,width=6,bg="red",relief=GROOVE,command=lambda:cleardisplay()).place(x=40,y=195)
zero = Button(text="  0  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(0)).place(x=115,y=195)
equal = Button(text=" = ",font=10,width=6,relief=GROOVE,command=lambda:Equal()).place(x=190,y=195)
add = Button(text="  +  ",font=10,width=6,bg="blue",relief=SOLID,command=lambda:btnclick("+")).place(x=265,y=195)
"""
e1 = Entry(width=27, font=8,borderwidth=3,textvariable=text_input).place(x=40,y=10)
b1 = Button(text="  1  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(1)).pack(pady=10)
b2 = Button(text="  2  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(2)).pack(pady=5)
b3 = Button(text="  3  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(3)).pack(pady=5)
devide = Button(text="  /  ",font=10,width=6,bg="blue",relief=SOLID,command=lambda:btnclick("/")).pack(pady=5)

b4 = Button(text="  4  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(4)).pack(pady=5)
b5 = Button(text="  5  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(5)).pack(pady=5)
b6 = Button(text="  6  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(6)).pack(pady=5)
multiply = Button(text="  x  ",font=10,width=6,bg="blue", relief=SOLID,command=lambda:btnclick("*")).pack(pady=5)

b7 = Button(text="  7  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(7)).pack(pady=5)
b8 = Button(text="  8  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(8)).pack(pady=5)
b9 = Button(text="  9  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(9)).pack(pady=5)
subtract = Button(text="  -  ",font=10,width=6,bg="blue",relief=SOLID,command=lambda:btnclick("-")).pack(pady=5)

dot = Button(text="  .  ",font=10,width=6,bg="red",relief=GROOVE,command=lambda:btnclick(".")).pack(pady=5)
zero = Button(text="  0  ",font=10,width=6,relief=GROOVE,command=lambda:btnclick(0)).pack(pady=5)
equal = Button(text=" = ",font=10,width=6,relief=GROOVE,command=lambda:equal()).pack(pady=5)
add = Button(text="  +  ",font=10,width=6,bg="blue",relief=SOLID).pack(pady=5)
"""


window.mainloop()
