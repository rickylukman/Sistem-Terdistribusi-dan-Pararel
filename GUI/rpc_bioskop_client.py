import xmlrpc.client
import tkinter as tk
from tkinter import *
from tkinter import font  as tkfont 
from tkinter import messagebox

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# class pengaturan tampilan
class Window(tk.Tk):
	"""docstring for Window"""
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.geometry(self)
		self.geometry("400x500+485+72")
		# self.val = StringVar()
		self.title('Ticketing Film')
		self.title_font = tkfont.Font(family='Helvetica', size=28, weight="bold")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		#  untuk nampilin halaman sebanyak kelas n 
		for F in (StartPage, PageOne): 
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			frame.grid(row=0, column=0, sticky="ensw")
		self.show_frame("StartPage")
	
	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

# class halaman beranda
class StartPage(tk.Frame):
	"""docstring for ClassName"""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		label = tk.Label(self, text="Welcome to XXI", font=controller.title_font, bg="black", fg="gold")
		label.pack(padx= 60, pady=100)
	
		label_note = tk.Label(self, text="FILM YANG SEDANG TAYANG",font=("arial",14,"bold"), fg="black")
		label_note.place(x=60, y=200)

		arr_film = s.ambilfilm() # ngambil array dari server
		# nampilin film yang tersedia dan jadwal tayang
		i = 0 
		for i in range(len(arr_film)):
			label_film = tk.Label(self, text=(arr_film[i][1],arr_film[i][2]), 
									relief= 'groove')
			label_film.pack(pady=10)
		
		# button untuk pesan dan keluar
		button_pesan = tk.Button(self, text='PESAN', relief='ridge',command=lambda: controller.show_frame("PageOne"),
								font=("arial",12,"bold"), bg="gold")
		button_pesan.pack(side="right", padx=40)
		button_exit = tk.Button(self, text='KELUAR',relief='ridge',command=self.exit, 
								bg="red", fg="white", font=("arial",12,"bold"))
		button_exit.pack(side="left", padx=40)

	# untuk keluar dari apps
	def exit(self):
		MsgBox = tk.messagebox.askquestion ('keluar','Apakah anda ingin keluar dari aplikasi?',icon = 'warning')
		if MsgBox == 'yes':
			self.quit()

# class halaman tampilan pemesanan
class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		
		# procedure untuk action klik
		# def onclick(args):
		# 	if ():
		# 		print("pesanan berhasil")

		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Pemesanan Tiket", font=controller.title_font, bg="black", fg="gold")
		label.pack(pady=10)
		label_film2 = tk.Label(self, text="Film", font=("arial", 15))
		label_film2.place(x=40, y=200)

		arr_film = s.ambilfilm() #ambil array film dari server
		# variabel utk nampung array
		daftarfilm = []
		totaltiket = []
		totalharga = []
		
		for i in range(len(arr_film)): 
			daftarfilm.append(arr_film[i][1]) 
			totalharga.append(arr_film[i][3])
			totaltiket.append(arr_film[i][4])

		# drop down pemilihan film
		film = StringVar() 
		film.set("Daftar Film")
		pilih_film = tk.OptionMenu(self, film, *daftarfilm) #untuk drop down
		pilih_film.config(width=25)
		# print(film.get()) 
		pilih_film.place(x= 160, y=200)

		# drop down pemilihan jam tayang
		daftarjam = [] # array untuk jam tayang
		label_jam = tk.Label(self, text="Jam Tayang", font=("arial", 15))
		label_jam.place(x=40, y=250)
		jam = StringVar()
		jam.set("Jam Tayang")

		for j in range(len(arr_film)):
			daftarjam.append(arr_film[j][2])
		pilih_jam = tk.OptionMenu(self, jam, *daftarjam) # nampilin drop down
		pilih_jam.config(width=25) # untuk mengatur ukuran
		pilih_jam.place(x= 160, y=250) # untuk mengatur posisi 

		# entry untuk menambahkan tiket
		label_jumlah = tk.Label(self, text="Jumlah Tiket", font=("arial",15))
		label_jumlah.place(x=40, y=300)
		jml_tiket = IntVar()
		jml_tiket_entry = tk.Entry(self, textvariable = jml_tiket, width=7)
		jml_tiket_entry.place(x=165, y=300)

		# procedure utk ngasih feedback
		def pesan():
			print(film.get() + " " + jam.get())

			har = 0
			for i in range(len(arr_film)):
				if (arr_film[i][1] == film.get()):
					har = totalharga[i]
			tothar = s.totalharga(har,jml_tiket.get())

			totet = 0
			for i in range(len(arr_film)):
				if (arr_film[i][1] == film.get()):
					totet = totaltiket[i]
			print(totet)
			print(jml_tiket.get())

			MsgBox = tk.messagebox.askquestion ('total harga',tothar)
			if MsgBox == 'yes':
				for i in range(len(arr_film)):
					if (arr_film[i][1] == film.get()):
						totaltiket[i] = s.updatetiket(film.get(),totet,jml_tiket.get())
						transaksi = s.simpantransaksi(film.get(),jml_tiket.get(),tothar)
						print(totaltiket[i])
				self.quit()
						# MsgBox = tk.messagebox.askquestion ('konfirmasi','Pembelian anda berhasil')
						# if MsgBox == 'yes':
						# 	command=lambda: controller.show_frame("StartPage")

		# button untuk kembali dan melakukan pemesanan
		button_back = tk.Button(self, text="Kembali", relief='ridge',
						command=lambda: controller.show_frame("StartPage"), font=("arial",12,"bold"), bg="gold")
		button_back.place(x=40, y=420)

		button_order = tk.Button(self, text="Buat Pesanan", relief='ridge',
						command=pesan, font=("arial",12,"bold"), bg="gold")
		button_order.place(x=240, y=420)

# main program
if __name__ == "__main__":
    app = Window()
    app.mainloop()