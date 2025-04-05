from tkinter import *

def to_celsius():
    f = float(fahrenheit_entry.get())
    celsius_entry.delete(0, END)
    celsius_entry.insert(0, (f - 32) * 5 / 9)

def to_fahrenheit():
    c = float(celsius_entry.get())
    fahrenheit_entry.delete(0, END)
    fahrenheit_entry.insert(0, c * 9 / 5 + 32)

window = Tk()
Label(window, text="Fahrenheit").grid(row=0, column=0)
Label(window, text="Celsius").grid(row=0, column=1)

fahrenheit_entry = Entry(window)
fahrenheit_entry.grid(row=1, column=0)
fahrenheit_entry.insert(0, "32")

celsius_entry = Entry(window)
celsius_entry.grid(row=1, column=1)
celsius_entry.insert(0, "0.0")

Button(window, text=">>>>", command=to_celsius).grid(row=2, column=0)
Button(window, text="<<<<", command=to_fahrenheit).grid(row=2, column=1)

window.mainloop()
