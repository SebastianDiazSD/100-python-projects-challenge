import sys
import os
import tkinter

# import tkMessageBox
top = tkinter.Tk()


def run():
    os.system('python band_name_generator.py')


B = tkinter.Button(top, text="Run", command=run)
B.pack()
top.mainloop()
