import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("1280x720")
window.title("Testing TKinter!")
window.iconbitmap("54 TKinter/icons/py_icns.icns")

# width es la cantidad de caracteres que ocupa la entrada de texto
entry = ttk.Entry(window, width=30)
entry.grid(row=0,column=0)

window.mainloop()
