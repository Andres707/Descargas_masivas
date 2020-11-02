import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk, messagebox  # Carga ttk (para widgets nuevos 8.5+)
# import tkFont
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')


class ventana:
    def __init__(self):
        # Hilo Ventana
        hiloVentana = threading.Thread(name='Hiloventana', target=self.ventana)
        hiloVentana.start()
        hiloVentana.join()

    def ventana(self):
        # <UI>
        _ventana = Tk()
        _ventana.geometry('400x320')
        _ventana.configure(bg='beige')
        _ventana.title('Descargas Masivas')
        # Variavbles TK
        self.varUrl = tk.StringVar(_ventana)
        self.varMin = tk.StringVar(_ventana)
        self.varMax = tk.StringVar(_ventana)
        self.varRuta = tk.StringVar(_ventana)
        # <tabs>
        tab_control = ttk.Notebook(_ventana)
        _home = ttk.Frame(tab_control)
        _status = ttk.Frame(tab_control)
        _download = ttk.Frame(tab_control)
        tab_control.add(_home, text='Inicio')
        tab_control.pack(expand=1, fill='both')
        tab_control.add(_status, text='Estado')
        tab_control.pack(expand=1, fill='both')
        tab_control.add(_download, text='Descarga')
        tab_control.pack(expand=1, fill='both')
        # label
        lblSaludo = Label(_home, text="Descargas Masivas", fg='black')
        lblPagina = Label(_home, text="URL animeFLV", fg='black')
        lblRangoMin = Label(_home, text="Rango Minimo", fg='black')
        lblRangoMax = Label(_home, text="Rango Maximo", fg='black')
        lblRuta = Label(_home, text="Ruta de guardado", fg='black')
        # textbox
        txtPagina = ttk.Entry(_home, justify=tk.LEFT, textvariable=self.varUrl)
        txtRangoMin = ttk.Entry(_home, justify=tk.LEFT, textvariable=self.varMin)
        txtRangoMax = ttk.Entry(_home, justify=tk.LEFT, textvariable=self.varMax)
        txtRuta = ttk.Entry(_home, justify=tk.LEFT, textvariable=self.varRuta)
        # btn
        btnInicio = ttk.Button(_home, text='Iniciar', command=self.roow)
        # position
        lblSaludo.place(x=150, y=0)
        lblPagina.place(x=0, y=40)
        txtPagina.place(x=90, y=40, height=20, width=300)
        lblRangoMin.place(x=0, y=70)
        txtRangoMin.place(x=90, y=70, height=20, width=50)
        lblRangoMax.place(x=150, y=70)
        txtRangoMax.place(x=240, y=70, height=20, width=50)
        lblRuta.place(x=0, y=100)
        txtRuta.place(x=110, y=100, height=20, width=280)
        btnInicio.place(x=0, y=150, height=40, width=150)
        # table Status
        self._tree = ttk.Treeview(_status)
        self._tree["columns"] = ("one", "two", "three")
        vsb = ttk.Scrollbar(_status, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(_status, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')
        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.column("#0", width=20, minwidth=50, stretch=tk.NO)
        self._tree.column("one", width=20, minwidth=50)
        self._tree.column("two", width=20, minwidth=50)
        self._tree.column("three", width=20, minwidth=50)
        self._tree.heading("#0", text="#", anchor=tk.W)
        self._tree.heading("one", text="Capitulo", anchor=tk.W)
        self._tree.heading("two", text="Estado", anchor=tk.W)
        self._tree.heading("three", text="URL de descarga", anchor=tk.W)
        self._tree.pack(side=tk.TOP, fill=tk.X)
        _ventana.mainloop()

    def addRow(self, row, folder):
        self._tree.insert(folder, "end", values=row)

    def addFolder(self, row):
        f = self._tree.insert("", 1, values=row)
        return f

    def roow(self):
        row = ["Temporada 1", 12, 120]
        f = self.addFolder(row)
        row = [1, 12, 120, 46]
        self.addRow(row, f)


if __name__ == '__main__':
    ventana()
