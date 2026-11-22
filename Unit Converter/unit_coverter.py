import tkinter as tk
root = tk.Tk()
root.title("Unit Converter")
root.configure(bg="grey15")
entry = tk.Entry(root, font=("Arial",18),justify="right", bg="grey25", fg="white") #this line makes the box where user types in
entry.grid(row=0, column=0, columnspan=2,padx=10, pady=10) # places the typing box at the top and streaches it across both columns padx make space left and right pady make top and bottom
result_label =tk.Label(root,text="Result", font=("Arial",20,"bold"), bg="grey15", fg="lightgreen")#shows the result in bold green
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
def kg_to_lb(): #coverts kilograms to pounds
    try:
        kg = float(entry.get())
        result_label.config(text=str(round(kg * 2.20462)) + " lb")
    except:
        result_label.config(text="Enter a number")

def lb_to_kg():
    try:
        lb = float(entry.get())
        result_label.config(text=str(round(lb / 2.20462, 2)) + "kg")
    except:
         result_label.config(text="Enter a number")
def c_to_f():
    try:
        c = float(entry.get())
        result_label.config(text=str(round(c* 9 / 5 + 32, 2)) + "F")
    except:
         result_label.config(text="Enter a number")
def f_to_c():
    try:
        f = float(entry.get())
        result_label.config(text=str(round((f-32) * 5 / 9, 2)) + "C")
    except:
        result_label.config(text="Enter a number")
#next line adds colours to the buttons
tk.Button(root, text="kg to lb", font=("Arial",14,"bold"), bg="royalblue", fg="white", activebackground="lightskyblue",command=kg_to_lb).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="lb to kg", font=("Arial",14,"bold"), bg="royalblue", fg="white", activebackground="lightskyblue",command=lb_to_kg).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="C to F", font=("Arial",14,"bold"), bg="royalblue", fg="white", activebackground="lightskyblue",command=c_to_f).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="F to C", font=("Arial",14,"bold"), bg="royalblue", fg="white", activebackground="lightskyblue",command=f_to_c).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()

