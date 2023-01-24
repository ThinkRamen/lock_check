import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Lock Check')
root.resizable(False, False)
# root.geometry("200x150")
root.eval('tk::PlaceWindow . center')
###
title = tk.Label(root, text='select an option:')
title.pack()
###
selection = ttk.Combobox(root, state='readonly', values=[
                         'lock check', 'lock check + audit'])
selection.pack()
selection.current(1)
###
button = ttk.Button(root, text='select')
button.pack()
root.mainloop()
###
