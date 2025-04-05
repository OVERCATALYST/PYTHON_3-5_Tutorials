from tkinter import *

def guess():
    global low, high, comp_guess
    comp_guess = (low + high) // 2
    label.config(text=f"Is it {comp_guess}?")

def too_small():
    global low
    low = comp_guess + 1
    guess()

def too_large():
    global high
    high = comp_guess - 1
    guess()

def correct():
    label.config(text=f"Guessed correctly: {comp_guess}")
    disable_buttons()

def disable_buttons():
    small_btn.config(state=DISABLED)
    large_btn.config(state=DISABLED)
    correct_btn.config(state=DISABLED)

def new_game():
    global low, high
    low = 1
    high = 100
    enable_buttons()
    guess()

def enable_buttons():
    small_btn.config(state=NORMAL)
    large_btn.config(state=NORMAL)
    correct_btn.config(state=NORMAL)

window = Tk()
low = 1
high = 100
comp_guess = 0

label = Label(window, text="")
label.pack()

small_btn = Button(window, text="Too Small", command=too_small)
small_btn.pack()

large_btn = Button(window, text="Too Large", command=too_large)
large_btn.pack()

correct_btn = Button(window, text="Correct", command=correct)
correct_btn.pack()

Button(window, text="New Game", command=new_game).pack()
new_game()

window.mainloop()
