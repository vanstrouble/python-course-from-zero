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

# Métodos de los eventos
def click_event(button):
    if button == 1:
        button1.config(text=f"Botón {button} presionado")
    elif button == 2:
        button2.config(text=f"Botón {button} presionado")
    elif button == 3:
        button3.config(text=f"Botón {button} presionado")
    elif button == 4:
        button4.config(text=f"Botón {button} presionado")

# Definición de los botones
button1 = tk.Button(window, text="Botón 1", command=lambda: click_event(button=1))
button1.grid(row=0, column=0, sticky="NSWE",padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)

# button2 = tk.Button(window, text="Botón 2", command=lambda: click_event(button=2))
# button2.grid(row=1, column=0, sticky="NSWE")

# button3 = tk.Button(window, text="Botón 3", command=lambda: click_event(button=3))
# button3.grid(row=0, column=1, sticky="NSWE")

# button4 = tk.Button(window, text="Botón 4", command=lambda: click_event(button=4))
# button4.grid(row=1, column=1, sticky="NSWE")

window.mainloop()
