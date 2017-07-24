import tkinter as tk
from klient import *


class WidokListaKlientow(tk.Frame):
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		
		top_frame = tk.Frame(self)
		input_wyszukaj = tk.Entry(top_frame)
		input_wyszukaj.grid(row=0, column=0)

		button_wyszukaj = tk.Button(top_frame, text="Wyszukaj")
		button_wyszukaj.grid(row=0, column=1)

		button_dodaj_klienta = tk.Button(top_frame, text="Dodaj klienta")
		button_dodaj_klienta.grid(row=0, column=3)

		bottom_frame = tk.Frame(self)
		label_id = tk.Label(bottom_frame, text="Id")
		label_id.grid(row=0, column=0)

		label_nazwa = tk.Label(bottom_frame, text="Nazwa klienta")
		label_nazwa.grid(row=0, column=1)

		label_akcja = tk.Label(bottom_frame, text="Akcje")
		label_akcja.grid(row=0, column=2)


		klienci = wczytaj_klientow()
		for i in range(len(klienci)):
			tk.Label(bottom_frame, text=klienci[i].id).grid(row=i+1, column=0)
			tk.Label(bottom_frame, text=klienci[i].nazwa).grid(row=i+1, column=1)
			tk.Button(bottom_frame, text="Wyswietl profil", command=lambda i=i: controller.wczytaj_uslugi(klienci[i].id)).grid(row=i+1, column=2)

		top_frame.pack()
		bottom_frame.pack()
