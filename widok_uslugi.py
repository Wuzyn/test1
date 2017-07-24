import tkinter as tk
from klient import *
from usluga import *

class WidokUslugi(tk.Frame):

	def __init__(self, parent, controller, klient_id):
		tk.Frame.__init__(self, parent)
		
		top_frame = tk.Frame(self)
		input_wyszukaj = tk.Entry(top_frame)
		input_wyszukaj.grid(row=0, column=0)

		button_wyszukaj = tk.Button(top_frame, text="Wyszukaj")
		button_wyszukaj.grid(row=0, column=1)

		button_dodaj_klienta = tk.Button(top_frame, text="Dodaj usluge")
		button_dodaj_klienta.grid(row=0, column=3)

		bottom_frame = tk.Frame(self)
		label_id = tk.Label(bottom_frame, text="Id")
		label_id.grid(row=0, column=0)

		label_nazwa = tk.Label(bottom_frame, text="Nazwa")
		label_nazwa.grid(row=0, column=1)

		label_opis = tk.Label(bottom_frame, text="Opis")
		label_opis.grid(row=0, column=2)

		label_cena = tk.Label(bottom_frame, text="Cena netto")
		label_cena.grid(row=0, column=3)

		label_termin = tk.Label(bottom_frame, text="Termin")
		label_termin.grid(row=0, column=4)

		uslugi = wczytaj_uslugi(klient_id)
		print(uslugi)

		top_frame.pack()
		bottom_frame.pack()

