from tkinter import *
import random

def check():
    global count
    guess = int(entry.get())
    count += 1
    if guess < number:
        result.set("Too small, try again")
    elif guess > number:
        result.set("Too large, try again")
    else:
        result.set(f"Correct! Total guesses: {count}")

def new_game():
    global number, count
    number = random.randint(1, 100)
    count = 0
    result.set("")
    entry.delete(0, END)

window = Tk()
number = random.randint(1, 100)
count = 0
result = StringVar()

Entry(window).pack()
entry = Entry(window)
entry.pack()

Button(window, text="Guess", command=check).pack()
Label(window, textvariable=result).pack()
Button(window, text="New Game", command=new_game).pack()

window.mainloop()
