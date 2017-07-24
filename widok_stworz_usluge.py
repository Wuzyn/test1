import tkinter as tk

class WidokStworzUsluge(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame(self, parent)

		tk.Label(self, text="Nazwa").grid(row=0, column=0)
		input_nazwa = tk.Entry(self)
		input_nazwa.grid(row=0, column=1)

		tk.Label(self, text="Opis").grid(row=1, column=0)
		input_opis = tk.Text(self)
		input_opis.grid(row=1, column=1)

		tk.Label(self, text="Cena netto").grid(row=2, column=0)
		input_cena = tk.Entry(self)
		input_cena.grid(row=2, column=1)

		tk.Label(self, text="Termin").grid(row=3, column=0)
		input_termin = tk.