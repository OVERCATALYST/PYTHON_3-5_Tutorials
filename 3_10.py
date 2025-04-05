from tkinter import *

def compute():
    h = float(height.get())
    b = float(bounce.get())
    n = int(bounces.get())
    total = h
    for i in range(1, n):
        h *= b
        total += 2 * h
    result.set(f"Total Distance: {total}")

window = Tk()
Label(window, text="Initial Height").grid(row=0, column=0)
Label(window, text="Bounciness Index").grid(row=1, column=0)
Label(window, text="Number of Bounces").grid(row=2, column=0)

height = Entry(window)
height.grid(row=0, column=1)
bounce = Entry(window)
bounce.grid(row=1, column=1)
bounces = Entry(window)
bounces.grid(row=2, column=1)

Button(window, text="Compute", command=compute).grid(row=3, column=0, columnspan=2)

result = StringVar()
Label(window, textvariable=result).grid(row=4, column=0, columnspan=2)

window.mainloop()
