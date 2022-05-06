from tkinter import *
from math import *

from pyparsing import col

root = Tk()
root.title("Calculator")

e = Entry(root,width = 35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(button):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(button))

def equal_button():
    expression = e.get()
    e.delete(0, END)
    try:
        e.insert(0, eval(expression))
    except SyntaxError:
        e.insert(0, "Make sure you closed the brackets")

def clear_button():
    e.delete(0, END)

button_1 = Button(root, text="1", padx = 50, pady = 20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx = 50, pady = 20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx = 50, pady = 20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx = 50, pady = 20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx = 50, pady = 20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx = 50, pady = 20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx = 50, pady = 20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx = 50, pady = 20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx = 50, pady = 20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx = 50, pady = 20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx = 49, pady = 20, command=lambda: button_click('+'))
button_subtract = Button(root, text="-", padx = 52, pady = 20, command=lambda: button_click('-'))
button_multiply = Button(root, text="*", padx = 51, pady = 20, command=lambda: button_click('*'))
button_divide = Button(root, text="/", padx = 51, pady = 20, command=lambda: button_click('/'))
button_sqrt = Button(root, text= "√", padx=50, pady=20, command=lambda:button_click('sqrt('))
#trigonometry functions
button_sin = Button(root, text="sin",padx=45, pady=20, command=lambda: button_click("sin("))
button_cos = Button(root, text="cos",padx=45, pady=20, command=lambda: button_click("cos("))
button_tan = Button(root, text="tan",padx=45, pady=20, command=lambda: button_click("tan("))
#brackets
button_open_parantheses = Button(root, text="(",padx = 51, pady = 20, command=lambda:button_click('('))
button_closed_parantheses = Button(root, text=")",padx = 50, pady = 20, command=lambda:button_click(')'))


button_equal = Button(root, text="=", padx = 108, pady = 20, command=equal_button)
button_clear = Button(root, text="clear", padx = 97, pady = 20, command=clear_button)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_sqrt.grid(row=7, column=0)
button_open_parantheses.grid(row=7, column=1)
button_closed_parantheses.grid(row=7, column=2)

button_sin.grid(row=8, column=0)
button_cos.grid(row=8, column=1)
button_tan.grid(row=8, column=2)


root.mainloop()