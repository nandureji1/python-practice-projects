import tkinter as tk #tkinter is given a nickname as tk
root = tk.Tk() #creates the main calculator window . Tk creates the window, its a tool in tkinter
root.title("My Calculator") #root is the window 
display = tk.Entry(root, font=("Arial",20),justify="right") #create cal display
display.grid(row=0, column=0,columnspan=4)
def press(value): #defines a function named press that hold a value
   display.insert(tk.END,value) #insert the pressed value at the end of display

def clear(): #this clear the whole display
   display.delete(0,tk.END)

def calculate(): 
   result = eval(display.get())# this performs the calculations
   clear()
   display.insert(0, result)
buttons = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "0", ".", "=", "+"]

row = 1
col = 0
for b in buttons:
   if b == "=":
      action = calculate
   else:
      action = lambda x=b: press(x)
   tk.Button(root, text=b, font=("Arial",18),width=4, command=action).grid(row=row, column=col)
   col += 1
   if col == 4:
      col = 0
      row += 1

tk.Button(root,text="C", font=("Arial",18),command=clear).grid(row=row, column=0, columnspan=4, sticky="we")

root.mainloop() #keeps the window open

 
