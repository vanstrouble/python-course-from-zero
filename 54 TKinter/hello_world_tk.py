# GUI
# TKinter: TK interface
import tkinter as tk  # Librería de tkinter
from tkinter import ttk  # Themes library for tkinter


window = tk.Tk()
window.geometry("1280x720")  # Tamaño de la ventana
window.title("Hello World Testing TKinter!")  # Nombre de la ventana
window.iconbitmap("54 TKinter/icons/py_ico.ico")  # Icono de la ventana
buttom1 = ttk.Button(window, text="Presioname")  # Crando un boton de la ventana
buttom1.pack()  # Colocando el boton en la ventana
window.mainloop()  # Mostrar la ventana
