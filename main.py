from tkinter import *
from math import *

#setting screen
window = Tk()
window.title("calculator")
window.geometry("800x400")
window.config(bg = "#213555")

#making grids
for i in range(8):
    window.grid_columnconfigure(index = i,weight = 1)
for i in range(7):
    window.grid_rowconfigure(index= i,weight = 1)

#let's store variables first
current_value = StringVar()
current_value.set("")

#set display
screen_label = Label(window, textvariable=current_value, bg="#FFFDEC", fg="black", font="Arial 20 bold", anchor="e")
screen_label.grid(row=0, column=0, columnspan=8, sticky="nsew", padx=10, pady=10)
screen_label.focus()


#lets create functions
def numbers_on_screen(number):
    num = current_value.get()
    current_value.set(num + str(number))

def symbols(symbol):
    sym = current_value.get()
    if sym:
        current_value.set(sym + str(symbol))

def clearing():
    on_screen = current_value.get()
    if on_screen:
        current_value.set("")

def remove_last():
    present_value = current_value.get()
    if present_value:
        current_value.set(present_value[:-1])

##let's handle special functions

def log_base10():
    value = current_value.get()
    if value:
        current_value.set(f"log({value})")

def ln_base_e():
    value = current_value.get()
    if value:
        current_value.set(f"ln({value})")

def trignometry_func(func):
    trig_value = current_value.get()
    if trig_value:
        current_value.set(f"{func}({trig_value})")

def pi_value():
    value = current_value.get()
    if value:
        current_value.set(f"{value}*(3.14)")

def e_value():
    value = current_value.get()
    if value:
        current_value.set(f"{value}*(2.71)")

def sq_root():
    value= current_value.get()
    if value:
        current_value.set(f"({value})**(0.5)")

def cube_root():
    value= current_value.get()
    if value:
        current_value.set(f"({value})**(1/3)")


#finally lets evaluate
def evaluate():
    expression = current_value.get()

    #let's replace few things
    expression = expression.replace("ln","log10")
    expression = expression.replace("ln","log")
    expression = expression.replace("^", "**")
    expression = expression.replace("sin", "sin(radians(")
    expression = expression.replace("cos", "cos(radians(")
    expression = expression.replace("tan", "tan(radians(")
    if "radians(" in expression:
        expression = expression.replace(")", ")))")


    try:
        result = eval(expression)
        current_value.set(str(result))
    except Exception as e:
        current_value.set("error")

#lets create buttons
Button(text = "7",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(7)).grid(row = 3,column = 0,sticky = "nsew")
Button(text = "8",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(8)).grid(row = 3,column = 1,sticky = "nsew")
Button(text = "9",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(9)).grid(row = 3,column = 2,sticky = "nsew")
Button(text = "4",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(4)).grid(row = 4,column = 0,sticky = "nsew")
Button(text = "5",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(5)).grid(row = 4,column = 1,sticky = "nsew")
Button(text = "6",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(6)).grid(row = 4,column = 2,sticky = "nsew")
Button(text = "1",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(1)).grid(row = 5,column = 0,sticky = "nsew")
Button(text = "2",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(2)).grid(row = 5,column = 1,sticky = "nsew")
Button(text = "3",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(3)).grid(row = 5,column = 2,sticky = "nsew")
Button(text = "0",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda: numbers_on_screen(0)).grid(row = 6,column = 0,sticky = "nsew")
Button(text = ".",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols(".")).grid(row = 6,column = 1,sticky = "nsew")
Button(text = "!",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("!")).grid(row = 6,column = 2,sticky = "nsew")
Button(text = "+",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("+")).grid(row = 3,column = 3,sticky = "nsew")
Button(text = "-",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("-")).grid(row = 4,column = 3,sticky = "nsew")
Button(text = "x",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("*")).grid(row = 5,column = 3,sticky = "nsew")
Button(text = "÷",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("/")).grid(row = 6,column = 3,sticky = "nsew")
Button(text = "log",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command=log_base10).grid(row = 3,column = 4,sticky = "nsew")
Button(text = "(",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("(")).grid(row = 4,column = 4,sticky = "nsew")
Button(text = ")",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols(")")).grid(row = 5,column = 4,sticky = "nsew")
Button(text = "=",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = evaluate).grid(row = 6,column = 4,sticky = "nsew")
Button(text = "sin",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:trignometry_func("sin")).grid(row = 3,column = 5,sticky = "nsew")
Button(text = "cos",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:trignometry_func("cos")).grid(row = 4,column = 5,sticky = "nsew")
Button(text = "tan",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:trignometry_func("tan")).grid(row = 5,column = 5,sticky = "nsew")
Button(text = "π",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = pi_value).grid(row = 6,column = 5,sticky = "nsew")
Button(text = "C",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = clearing).grid(row = 3,column = 6,sticky = "nsew")
Button(text = "ln",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = ln_base_e).grid(row = 4,column = 6,sticky = "nsew")
Button(text = "e",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = e_value).grid(row = 5,column = 6,sticky = "nsew")
Button(text = "%",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command =lambda:symbols("%") ).grid(row = 6,column = 6,sticky = "nsew")
Button(text = "⌫",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = remove_last).grid(row = 3,column = 7,sticky = "nsew")
Button(text = "^",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = lambda:symbols("^")).grid(row = 4,column = 7,sticky = "nsew")
Button(text = "√",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command = sq_root).grid(row = 5,column = 7,sticky = "nsew")
Button(text = "∛",bg = "#FFFDEC",fg = "black",padx = 2,pady = 2,highlightthickness= 1,font = "Arial 20 bold",command= cube_root).grid(row = 6,column = 7,sticky = "nsew")

window.mainloop()