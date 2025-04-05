from tkinter import *

def convert():
    result.delete(0, END)
    result.insert(0, text_entry.get().upper())

window = Tk()
text_entry = Entry(window)
text_entry.pack()

Button(window, text="Convert", command=convert).pack()
result = Entry(window)
result.pack()

window.mainloop()
