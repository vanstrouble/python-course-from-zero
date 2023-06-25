import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("600x400")
window.title("Manejo de grid")
window.iconbitmap("54 TKinter/icons/py_icns.icns")

# Métodos de los eventos
def clic_event(button):
    if button == 1:
        button1.config(text=f"Botón {button} presionado")
    elif button == 2:
        button2.config(text=f"Botón {button} presionado")
    elif button == 3:
        button3.config(text=f"Botón {button} presionado")
    elif button == 4:
        button4.config(text=f"Botón {button} presionado")

# Definición de los botones
button1 = tk.Button(window, text="Botón 1", command=lambda: clic_event(button=1))
button1.grid(row=0, column=0, sticky="W")

button2 = tk.Button(window, text="Botón 2", command=lambda: clic_event(button=2))
button2.grid(row=1, column=0, sticky="W")

button3 = tk.Button(window, text="Botón 3", command=lambda: clic_event(button=3))
button3.grid(row=0, column=1, sticky="W")

button4 = tk.Button(window, text="Botón 4", command=lambda: clic_event(button=4))
button4.grid(row=1, column=1, sticky="W")

window.mainloop()
