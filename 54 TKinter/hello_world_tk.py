# GUI
# TKinter: TK interface
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("1280x720")
window.title("Testing TKinter!")
window.iconbitmap("54 TKinter/icons/py_icns.icns")

def clic_event():
    buttom1.config(text="Tócame más fuerte")
    print("Presionas muy duro")
    button2 = ttk.Button(window, text="Nuevo botón")
    button2.pack()

buttom1 = ttk.Button(window, text="No presiones el botón", command=clic_event)
buttom1.pack()

window.mainloop()