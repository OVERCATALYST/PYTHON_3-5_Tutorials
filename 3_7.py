from tkinter import *
from tkinter import messagebox
import math

def compute():
    try:
        num = int(entry.get())
        result.delete(0, END)
        result.insert(0, math.sqrt(num))
    except:
        messagebox.showerror("Error", "Invalid input")

window = Tk()
entry = Entry(window)
entry.pack()

Button(window, text="Compute", command=compute).pack()
result = Entry(window)
result.pack()

window.mainloop()
