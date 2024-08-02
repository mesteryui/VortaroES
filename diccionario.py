import tkinter as tk
from tkinter import *
import webbrowser as wb

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Diccionario")
entry = tk.Entry(ventana, width=30)
entry.pack()
def busqueda():
    text = entry.get()
    text_final = "https://dle.rae.es/" + text
    wb.open(text_final)


button = tk.Button(ventana,text="Buscar", command=busqueda)
button.pack()
ventana.mainloop()
