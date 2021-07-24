from tkinter import *

import time

root = Tk()
root.title('Digital clock with day and month')
root.geometry("600x400")


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")
    month_name = time.strftime("%B")
    year = time.strftime("%Y")
    date = time.strftime("%c")

    my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    my_label.after(1000, clock)

    my_label2.config(text=time_zone + "     " + day + "   " + "   " + month_name + "   " + year)

    my_label3.config(text=date)


def update():
    my_label.config(text="New Text")


my_label = Label(root, text="", font=("times", 50, "bold"), fg="green", bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("times", 14))
my_label2.pack(pady=5)

my_label3 = Label(root, text="", font=("times", 14))
my_label3.pack(pady=5)

clock()

root.mainloop()
