# Application published under GPL-3.0 or superior the program is distributed without any warranty you should have recived a copy of GNU General Public License with this program if not see https://www.gnu.org/licenses/
import tkinter as tk
from tkinter import *
import webbrowser as wb
import re
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("VortaroES")
entry = tk.Entry(ventana, width=30)
entry.pack()
def busqueda():
    text = entry.get()
    if text == "":
        return
    elif re.match(r'^\d+(?:,\d+)*(?:\.\d+)?$', text):
        return
    elif re.match(r'^[+-]?\d+(?:,\d+)*([+\-*].\d+)?$|^\d+$', text):
        return
    else:
        text_final = "https://dle.rae.es/" + text
        wb.open(text_final)


button = tk.Button(ventana,text="Buscar", command=busqueda)
button.pack()
license = Label(ventana, text="Licenciado bajo GPL-3.0 o superior")
license.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
ventana.mainloop()
