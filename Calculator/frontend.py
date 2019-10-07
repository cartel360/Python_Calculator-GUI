from tkinter import *
import math

expression = ""

def getandreplace(self):
    self.expression = self.e.get()
    self.newtext = expression.replace('÷','/')
    self.newtext = newtext.replace('x','*')

def press(num):
    global expression
    expression = expression + str(num)
    equation.set (expression)


def equalpress():
    try:
        global expression
        total = eval(expression)
        equation.set(total)
        expression = ""
    except SyntaxError or NameError:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression=expression_field.get()[:-1]
    expression_field.delete(0,END)
    expression_field.insert(0,expression)

def clearall():
    global expression
    expression=expression_field.get()[:0]
    expression_field.delete(0, END)


def squareroot():
    try:
        global expression
        squareroot=math.sqrt(int(expression))
        equation.set(squareroot)
        expression=""
    except SyntaxError or NameError:
        equation.set("Error")
        expression=""

def square():
    try:
        global expression
        square=math.pow(int(expression.value,2))
        equation.set(square)
        expression=""
    except SyntaxError or NameError:
        equation.set("Error")
        expression=""


window=Tk()
window.configure(background="grey")
equation = StringVar()
window.wm_title("Calulator")



expression_field = Entry(window,relief=RIDGE, textvariable = equation,bd=15,bg='powder blue')
expression_field.grid(row=0,column=0,rowspan=2,columnspan=4,ipadx=50,pady=10)


b01=Button(window,text="%",command=lambda:press('%'),height=2,width=7)
b01.grid(row=2,column=0)

b01=Button(window,text="x²",command=square,height=2,width=7)
b01.grid(row=2,column=1)

b01=Button(window,text="(",command=lambda:press('('),height=2,width=7)
b01.grid(row=2,column=2)

b01=Button(window,text=")",command=lambda:press(')'),height=2,width=7)
b01.grid(row=2,column=3)

b1=Button(window,text="CE",command=clearall,height=2,width=7)
b1.grid(row=3,column=0)

b2=Button(window,text="C",command=clear,height=2,width=7)
b2.grid(row=3,column=1)

b3=Button(window,text="√",command=squareroot,height=2,width=7)
b3.grid(row=3,column=2)

b4=Button(window,text="÷",command=lambda:press("/"),height=2,width=7)
b4.grid(row=3,column=3)

b5=Button(window,text="7",command=lambda:press(7),height=2,width=7)
b5.grid(row=4,column=0)

b6=Button(window,text="8",command=lambda:press(8),height=2,width=7)
b6.grid(row=4,column=1)

b7=Button(window,text="9",command=lambda:press(9),height=2,width=7)
b7.grid(row=4,column=2)

b8=Button(window,text="x",command=lambda:press("*"),height=2,width=7)
b8.grid(row=4,column=3)

b9=Button(window,text="4",command=lambda:press(4),height=2,width=7)
b9.grid(row=5,column=0)

b10=Button(window,text="5",command=lambda:press(5),height=2,width=7)
b10.grid(row=5,column=1)

b11=Button(window,text="6",command=lambda:press(6),height=2,width=7)
b11.grid(row=5,column=2)

b12=Button(window,text="+",command=lambda:press("+"),height=2,width=7)
b12.grid(row=5,column=3)

b13=Button(window,text="1",command=lambda:press(1),height=2,width=7)
b13.grid(row=6,column=0)

b14=Button(window,text="2",command=lambda:press(2),height=2,width=7)
b14.grid(row=6,column=1)

b15=Button(window,text="3",command=lambda:press(3),height=2,width=7)
b15.grid(row=6,column=2)

b16=Button(window,text="-",command=lambda:press("-"),height=2,width=7)
b16.grid(row=6,column=3)

b17=Button(window,text="OFF",command=window.destroy,height=2,width=7)
b17.grid(row=7,column=0)

b17=Button(window,text="0",command=lambda:press(0),height=2,width=7)
b17.grid(row=7,column=1)

b18=Button(window,text=".",command=lambda:press("."),height=2,width=7)
b18.grid(row=7,column=2)

b16=Button(window,text="=",command=equalpress,height=2,width=7)
b16.grid(row=7,column=3)






window=mainloop()
