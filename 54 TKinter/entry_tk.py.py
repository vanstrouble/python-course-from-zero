import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("600x400")
window.title("Manejo de grid")
window.iconbitmap("54 TKinter/icons/py_icns.icns")

# Configuración del grid
window.rowconfigure(0, weight=2)
window.rowconfigure(1, weight=10)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)



window.mainloop()
