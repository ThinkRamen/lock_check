import tkinter as tk
from tkinter import ttk
from lock_check import lock_check_json, get_auth
from audit import audit_json
import sys

# functions


def make_selection():
    get_auth()
    text.insert(1.0, audit_json())
    text.insert(1.0, lock_check_json())
    ###
# classes

# main


root = tk.Tk()
text = tk.Text()
root.title('Lock Check')
root.resizable(False, False)
# root.geometry("200x150")
root.eval('tk::PlaceWindow . center')
###
title = tk.Label(root, text='select an option:').pack()
###
selection = ttk.Combobox(root, state='readonly', values=[
    'lock check', 'lock check + audit'])
selection.pack()
selection.current(1)
text = tk.Text(root)
text.pack()


button = ttk.Button(root, text='select', command=make_selection)
button.pack()

root.mainloop()


###
