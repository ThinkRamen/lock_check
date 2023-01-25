'''
Creates GUI window for txt field output and option selection.
'''
# imports
import tkinter as tk
from tkinter import ttk
from lock_check import lock_check_json, get_auth, to_txt_file
from audit import audit_json
from lock_check_old import firefox_automation
import os

# functions


def make_selection():
    get_auth()
    text.config(state='normal')
    text.delete("1.0", "end")
    if selection.get() == 'lock check':
        lock_check = lock_check_json()
        text.insert(0.0, lock_check)
        to_txt_file(lock_check)
        text.insert(0.0, '\n')
    if selection.get() == 'lock check + audit':
        lock_check = lock_check_json()
        audit = audit_json()
        text.insert('end', lock_check)
        text.insert('end', '\n')
        text.insert('end', audit)
        to_txt_file(lock_check + audit)
    if selection.get() == 'lock check + audit (old)':
        lock_check = lock_check_json()
        audit = audit_json()
        text.insert('end', lock_check)
        text.insert('end', '\n')
        text.insert('end', audit)
        firefox_automation(to_txt_file(lock_check + audit))

    text.config(state='disabled')
    ###


root = tk.Tk()
text = tk.Text()
root.title('Lock Check')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
title = tk.Label(root, text='select an option:').pack()
selection = ttk.Combobox(root, state='readonly', values=[
    'lock check', 'lock check + audit', 'lock check + audit (old)'])
selection.pack()
selection.current(1)
text = tk.Text(root, state='disabled')
text.pack()
button = ttk.Button(root, text='select', command=make_selection)
button.pack()

root.mainloop()
###
