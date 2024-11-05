"""
Copyright (c) 2024, <Mester>

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
# Librerias a importar
import tkinter as tk
from tkinter import ttk
import tkinterweb
import urllib.parse
import re
from catppuccin import PALETTE


# Funcion principal de busqueda
def busqueda():
    # Obtencion de entrada
    text = entry.get()
    # Sistema para evitar que se busque texto que no tiene sentido buscar
    if text == "":
        return
    elif re.match(r'^\d+(?:,\d+)*(?:\.\d+)?$', text):
        print("omit")
        return
    elif re.match(r'^[+-]?\d+(?:,\d+)*([+\-*].\d+)?$|^\d+$', text):
        print("omit")
        return
    # En caso de que el texto si tenga sentido
    else:
        text_final = "https://dle.rae.es/" + urllib.parse.quote(text)
        webframe.load_website(text_final)

if __name__ == "__main__":
    color_fondo = PALETTE.mocha.colors.base.hex
    color_base = PALETTE.mocha.colors.mantle.hex
    color_texto = PALETTE.mocha.colors.text.hex
    color_boton = PALETTE.mocha.colors.surface2.hex
    color_boton_activo = PALETTE.mocha.colors.surface1.hex
    ventana = tk.Tk()
    estilo_elementos = ttk.Style()
    # Configuraciones de estilo para diversos elementos
    estilo_elementos.configure("TLabel", background=color_fondo, foreground=color_texto)
    estilo_elementos.configure("TButton", background=color_boton, foreground=color_texto)
    estilo_elementos.map("TButton", background=[("active", color_boton_activo)], foreground=[("active", color_texto)])
    # Ajustes diversos de la ventana
    ventana.geometry("750x720")
    ventana.title("VortaroES")
    ventana["bg"] = color_fondo
    entry = ttk.Entry(ventana, width=30)
    entry.pack()
    frame = ttk.Frame(ventana,height=380, width=499)
    webframe = tkinterweb.HtmlFrame(frame)
    button = ttk.Button(ventana,text="Buscar", command=busqueda)
    button.pack()
    frame.pack(expand=False)
    webframe.pack()
    ventana.mainloop()
    
