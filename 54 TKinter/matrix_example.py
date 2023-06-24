import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("600x400")
window.title("Manejo de grid")
window.iconbitmap("54 TKinter/icons/py_icns.icns")

# Métodos de los eventos
def event1():
    button1.config(text="Botón 1 presionado")

def event2():
    button2.config(text="Botón 2 presionado")

# Definición de los botones
button1 = tk.Button(window, text="Botón 1", command=event1)
button1.grid(row=0, column=0)

button2 = tk.Button(window, text="Botón 2", command=event2)
button2.grid(row=1, column=0)

window.mainloop()