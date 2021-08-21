from tkinter import *
import os


def close():
    root.destroy()


def launch():
    os.system('python main.py')


def result():
    f = open('./scan/Correct plates.txt')
    text = f.read()
    print(text)
    result_label.config(text=text, bg='white')


root = Tk()
root.minsize(800, 600)
root.title("Real-Time Number Plate Recognition")
root.configure(bg="light blue")

title = Label(root, text="Real-Time Number Plate Recognition", bg='grey', font=('Ariel', 20))
title.pack()

instructions = Label(root, text="Press Q to save snap when number plate is detected,\n Press E to exit program",
                     bg='grey')
instructions.pack()

close_btn = Button(root, text="Close", command=close, fg="white", bg="red")
close_btn.place(relx=1.0, rely=0.0, anchor='ne')

launch_btn = Button(root, text="Launch", command=lambda: launch(), bg='light blue')
launch_btn.pack(padx=10, pady=10)

result_btn = Button(root, text="Result", command=lambda: result(), bg='light blue')
result_btn.pack(padx=10, pady=10)

result_label = Label(root, text='', bg='light blue')
result_label.pack()

root.mainloop()
