import tkinter as tk
from widok_lista_klientow import WidokListaKlientow
from widok_uslugi import WidokUslugi

class MainApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.container = tk.Frame(self)

		self.container.pack(side="top", fill="both", expand=True)

		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		#self.frames = {}

		#for F in (WidokListaKlientow, WidokUslugi):
		#	frame = F(container, self)
		#	self.frames[F] = frame
		#	frame.grid(row=0, column=0, sticky="nsew")

		self.wczytaj_klientow()

	#def show_frame(self, cont):
	#	frame = cont(self.container, self)
	#	frame.grid(row=0, column=0, sticky="nsew")
	#	frame.tkraise()

	def wczytaj_uslugi(self, klient_id):
		frame = WidokUslugi(self.container, self, klient_id)
		frame.grid(row=0, column=0, sticky="nsew")
		frame.tkraise()

	def wczytaj_klientow(self):
		frame = WidokListaKlientow(self.container, self)
		frame.grid(row=0, column=0, sticky="nsew")
		frame.tkraise()		

root = MainApp()
root.mainloop()
