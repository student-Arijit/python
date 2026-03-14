#Write a program to find whether a number is odd or even.

from tkinter import *

root = Tk()
root.geometry("250x200")
root.resizable(False, False)

l = Label(root, text="")
l.place(x=10, y=60)

def eve_odd():
    try:
        x = int(num.get())
        res = "even" if x % 2 == 0 else "odd"
        l.config(text=f"The number is a {res} number.")
    except ValueError:
        l.config(text="Please Enter a Number!!!")

label = Label(root, text="Enter a number: ")
label.place(x=10, y=5)
num = Entry(root)
num.place(x=100, y=5)
btn = Button(root, text="Submit", command=eve_odd)
btn.place(x=100, y=35)

root.mainloop()
