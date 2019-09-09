from tkinter import * 


def CreateTab(form):
    rows = 0
    while rows < 50:
        form.rowconfigure(rows, weight=1)
        form.columnconfigure(rows, weight=1)
        rows += 1
 
    # Defines and places the notebook widget
    nb = ttk.Notebook(form)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
    # Adds tab 1 of the notebook
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Tab1')
 
    # Adds tab 2 of the notebook
    page2 = ttk.Frame(nb)
    nb.add(page2, text='Tab2')
    