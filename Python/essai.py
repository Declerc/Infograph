# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:55:53 2020

@author: gomesdat
"""



import tkinter as tk

def callback(event):
    print(event.widget['text'])
    print(event.widget.extra)

main = tk.Tk()

switcher = tk.Label(main, text="click here")
switcher.grid()
switcher.bind("<Button-1>", callback)
switcher.extra = "Hello"
print(switcher.extra)
main.mainloop()