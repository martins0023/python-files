#NOTE)_
#TKINTER GUI CALCULATOR
#RUN python tkcalculator.py TO EXECUTE FILE
#ADD, RE-EDIT AND REFORM
#MODULES - TKINTER


from dis import dis
import math
from tkinter import *

from click import command

root = Tk()
root.resizable(False, False)
root.title("My calculator")
root.configure(bg="black")

e = Entry(root, width=48, bg="black", fg="white")
e.grid(row=0, columnspan=4, ipady=23)

#HISTORY
var = StringVar()
var2 = StringVar()
###############3
frame = Frame(root, width=20, bg="black")#frame
frame.grid( column=5, rowspan=7, ipady=220)

###############################
e2 = Label(frame, textvariable=var, width=20, bg="black", fg="white")#label
e2.grid(column=5, row=2, rowspan=7, pady=3)#label placement

###############
label_final_ans = Label(frame, textvariable=var2, width=20, bg="black", fg="white")
label_final_ans.grid(column=5, row=10, rowspan=7)
#e2 = Label(root, textvariable=var, width=20, bg="white", fg="black")
#e2.grid(column=5, row=0, rowspan=7, ipady=220)


def button_insert(number):
    global current
    global e
    global e2
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def addition():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    global sign_
    op = "add"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))

def subtraction():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "subtract"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def multiplication():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "multiply"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def division():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "divide"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def factorial():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "factorize"
    first_num = e.get()
    e.delete(0, END)
    var.set( str(first_num))
    
def percent():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "percentage"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def square_root():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "square_rt"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def square():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "sqr"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def cube():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "cub"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))

def cuberoot():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "cubert"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def inverse():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "inv"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))

def pie():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "pi"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def delete_entry():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global sign_
    op = "del_entry"
    e.delete(0,END)
    
def cosine():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "cos_ine"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))

def tangent():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "tan_gent"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))

def sine():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global var
    op = "s_ine"
    first_num = e.get()
    e.delete(0,END)
    var.set( str(first_num))
    
def equal():
    global current
    global e
    global first_num
    global s_num
    global the_sum
    global op
    global sign_
    s_num = e.get()
    if op == "add":
        e.delete(0,END)
        equal = int(first_num) + int(s_num)
        e.insert(0, int(equal))
        dis = f"{first_num } + {s_num}"
        sign = f" = {equal}"
        var.set( dis)
        var2.set(sign)
    elif op == "subtract":
        e.delete(0,END)
        equal = int(first_num) - int(s_num)
        e.insert(0, int(equal))
        dis = f"{first_num } - {s_num}"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "multiply":
        e.delete(0,END)
        equal = int(first_num) * int(s_num)
        e.insert(0, int(equal))
        dis = f"{first_num } * {s_num}"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "divide":
        e.delete(0,END)
        equal = int(first_num) / int(s_num)
        e.insert(0, float(equal))
        dis = f"{first_num } / {s_num}"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "factorize":
        e.delete(0, END)
        equal = (int(first_num) * (int(first_num) - 1))
        e.insert(0, int(equal))
        dis = f"{first_num } * {s_num} - 1"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "percentage":
        e.delete(0, END)
        percent_age = int(first_num) / 100
        equal = percent_age
        e.insert(0, float(equal))
        dis = f"{first_num }  %"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "square_rt":
        e.delete(0, END)
        equal = int(1/first_num) * 100
        e.insert(0, int(equal))
        var.set( equal)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "sqr":
        e.delete(0, END)
        equal = int(first_num) * int(first_num)
        e.insert(0, int(equal))
        dis = f"{first_num }²"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "cub":
        e.delete(0, END)
        equal = int(first_num) * int(first_num) * int(first_num)
        dis = f"{first_num }\u00b3"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "cube_rt":
        e.delete(0, END)
        equal = int(1/first_num) * 100
        e.insert(0, int(equal))
        var.set( equal)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "inv":
        e.delete(0, END)
        equal = 1/int(first_num)
        e.insert(0, float(equal))
        var.set( equal)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "pi":
        e.delete(0, END)
        equal = int(first_num) * 3.1429
        e.insert(0, float(equal))
        dis = f"{first_num } π"
        var.set( dis)
        sign = f" = {equal}"
        var2.set(sign)
    elif op == "s_ine":
        e.delete(0, END)
        equal = sine(int(first_num)) 
        e.insert(0, float(equal))
        var.set( equal)
            
    else:
        pass
        
def sign():
    pass
        

button_1 = Button(root, text="1", bg="black", fg="white", padx=42, pady=20, command=lambda:button_insert(1))
button_2 = Button(root, text="2", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(2))
button_3 = Button(root, text="3", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(3))
button_4 = Button(root, text="4", bg="black", fg="white", padx=42, pady=20, command=lambda:button_insert(4))
button_5 = Button(root, text="5", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(5))
button_6 = Button(root, text="6", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(6))
button_7 = Button(root, text="7", bg="black", fg="white", padx=42, pady=20, command=lambda:button_insert(7))
button_8 = Button(root, text="8", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(8))
button_9 = Button(root, text="9", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(9))
button_0 = Button(root, text="0", bg="black", fg="white", padx=40, pady=20, command=lambda:button_insert(0))

button_add = Button(root, text="+", bg="black", fg="white", padx=40, pady=20, command=addition)
button_sub = Button(root, text="-", bg="black", fg="white", padx=43, pady=20, command=subtraction)
button_multiply = Button(root, text="*", bg="black", fg="white", padx=42, pady=20, command=multiplication)
button_division = Button(root, text="/", bg="black", fg="white", padx=42, pady=20, command=division)
button_equal = Button(root,text="=", bg="light blue", fg="white", padx=39, pady=20, activebackground="black", activeforeground="red", command=equal)

button_factorial = Button(root,text="x!", bg="black", fg="white", padx=41, pady=21, command=factorial)
button_point = Button(root,text=".", bg="black", fg="white", padx=44, pady=22)

button_clear = Button(root, text="C", bg="silver", fg="white", padx=41, pady=20, command=delete_entry, activebackground="red", activeforeground="black")
button_percent = Button(root, text="%", bg="black", fg="white", padx=41, pady=20, command=percent)
button_square_root = Button(root, text="\u221ax", bg="black", fg="white", padx=37, pady=21, command=square_root)
button_square = Button(root, text="x\u00b2", bg="black", fg="white", padx=37, pady=21, command=square)

button_cube = Button(root, text="x\u00b3", bg="black", fg="white", padx=39, pady=22, command=cube)
button_cuberoot = Button(root, text="3\u221ax", bg="black", fg="white", padx=32, pady=22, command=cuberoot)
button_inverse = Button(root, text="x⁻¹", bg="black", fg="white", padx=34, pady=22, command=inverse)
button_pie = Button(root, text="π", bg="black", fg="white", padx=40, pady=22, command=pie)

button_cos = Button(root, text="cos", bg="black", fg="white", padx=35, pady=22, command=cosine)
button_tan = Button(root, text="tan", bg="black", fg="white", padx=35, pady=22, command=tangent)
button_sin = Button(root, text="sin", bg="black", fg="white", padx=35, pady=22, command=sine)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)

button_division.grid(row=4, column=3)
button_0.grid(row=4, columnspan=3)
button_clear.grid(row=4, column=2)
button_percent.grid(row=4, column=0)

button_factorial.grid(row=5, column=0)
button_point.grid(row=5, column=1)
button_square_root.grid(row=5, column=2)
button_square.grid(row=5, column=3)

button_cube.grid(row=6, column=0)
button_cuberoot.grid(row=6, column=1)
button_inverse.grid(row=6, column=2)
button_pie.grid(row=6, column=3)

button_cos.grid(row=7, column=0)
button_tan.grid(row=7, column=1)
button_sin.grid(row=7, column=2)
button_equal.grid(row=7, column=3)
root.mainloop()