from tkinter import *

def run():
    name1 = name_storage.get()
    print(name1)
    name.delete(0, END)

screen = Tk()
screen.title("my firt grapichs program")
screen.geometry("500x500")

welcome_text = Label(text = "Welcome to our first grapichs program ", fg = "red", bg = "yellow")
welcome_text.pack()

click_me = Button(text = "click me", fg = "red", bg = "yellow", command = run)
click_me.place(x = 10, y = 20)

name_storage = StringVar()
name = Entry(textvariable = name_storage)
name.pack()
screen.mainloop()