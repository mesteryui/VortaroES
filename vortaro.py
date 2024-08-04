"""
Copyright (c) 2024, <Nombre del Autor>

This program is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or 
(at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""
import tkinter as tk
from tkinter import *
#import webbrowser as wb
import tkinterweb
import urllib.parse
import re

def busqueda():
    text = entry.get()
    if text == "":
        return
    elif re.match(r'^\d+(?:,\d+)*(?:\.\d+)?$', text):
        print("omit")
        return
    elif re.match(r'^[+-]?\d+(?:,\d+)*([+\-*].\d+)?$|^\d+$', text):
        print("omit")
        return
    else:
        text_final = "https://dle.rae.es/" + urllib.parse.quote(text)
        #wb.open(text_final)
        webframe.load_website(text_final)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("750x720")
    ventana.title("VortaroES")
    entry = tk.Entry(ventana, width=30)
    entry.pack()

    frame = tk.Frame(ventana,height=380, width=499)
    webframe = tkinterweb.HtmlFrame(frame)

    button = tk.Button(ventana,text="Buscar", command=busqueda)
    button.pack()
    frame.pack(fill=None, expand=False)
    webframe.pack()
    license = Label(ventana, text="Licenciado bajo GPL-3.0 o superior")
    license.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
    ventana.mainloop()
