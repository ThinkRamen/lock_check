'''
Creates GUI window for txt field output and option selection.
'''
# imports
import tkinter as tk
from tkinter import ttk
from lock_check import lock_check_json, get_auth
from audit import audit_json
import sys

# functions


def make_selection():
    get_auth()
    text.config(state='normal')
    text.delete("1.0", "end")
    if selection.get() == 'lock check':
        text.insert(0.0, lock_check_json())
        text.insert(0.0, '\n')
    if selection.get() == 'lock check + audit':
        text.insert('end', lock_check_json())
        text.insert('end', '\n')
        text.insert('end', audit_json())
    text.config(state='disabled')
    ###


root = tk.Tk()
text = tk.Text()
root.title('Lock Check')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
title = tk.Label(root, text='select an option:').pack()
selection = ttk.Combobox(root, state='readonly', values=[
    'lock check', 'lock check + audit'])
selection.pack()
selection.current(1)
text = tk.Text(root, state='disabled')
text.pack()
button = ttk.Button(root, text='select', command=make_selection)
button.pack()

root.mainloop()
###
