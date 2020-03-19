import xmlrpc.client

#hanya untuk admin
#connect server
s = xmlrpc.client.ServerProxy('http://192.168.1.4:8000')

i = 1
while (i != 0):
	print("Menu admin")
	print("1. Lihat transaksi")
	print("2. Edit Studio")
	print("3. Tambah film")
	print("0. Exit")
	i = int(input("Pilihan=")) #input untuk memilih pilihan menu
	if (i == 1): #menu untuk melihat informasi transaksi berhasil pelanggan
		transaksi = s.ambiltransaksi()
		for x in range(len(transaksi)):
			print(x+1, transaksi[x])
	elif (i == 2): #menu edit informasi studio
		bioskop = s.ambilfilm()
		for i in range(len(bioskop)):
			if (bioskop[i][4] != 0):
				print(bioskop[i][0], bioskop[i][1],' tayang pada pukul ',bioskop[i][2])
		print("Menu edit")
		print("1. Edit film studio 1")
		print("2. Edit film studio 2")
		print("3. Edit film studio 3")
		print("0. Kembali")
		i = int(input("Pilihan="))
		print("-----------------------------------------------")
		if (i != 0):
			studio = i-1
			n = 1
			while (n != 0):
				print("Tentang Studio:")
				print(bioskop[studio])
				print("Menu Film")
				print("1. Ubah Film")
				print("2. Ubah Jam tayang")
				print("3. Ubah harga")
				print("4. Ubah tiket")
				print("0. Kembali")
				n = int(input("Pilihan="))
				if (n == 1):
					bioskop[studio][1] = input("Nama Film:")
				elif (n==2):
					bioskop[studio][2] = input("Jam tayang:")
				elif (n==3):
					bioskop[studio][3] = input("Harga:")
				elif (n==4):
					bioskop[studio][4] = input("Tiket:")
				bioskop = s.updatestudio(bioskop[studio][0],bioskop[studio][1],bioskop[studio][2],bioskop[studio][3],bioskop[studio][4])
	elif (i == 3):
		bioskop = s.ambilfilm()
		print("Tambah film")
		ss = input("Studio: ")
		judulf = input("Judul: ")
		jamt = input("Jam: ")
		hargaf = int(input("Harga: "))
		tiketf = int(input("Tiket: "))
		bioskop = s.tambahfilm(ss,judulf,jamt,hargaf,tiketf)
		# if (bioskop == null):
		# 	print("Tambah film")
		# 	ss = input("Studio: ")
		# 	judulf = input("Judul: ")
		# 	jamt = input("Jam: ")
		# 	hargaf = input("Harga: ")
		# 	tiketf = input("Tiket: ")
		# 	bioskop = s.tambahfilm(ss,judulf,jamt,hargaf,tiketf)
		# else:
		# 	print("Tambah film")
		# 	ss = input("Studio: ")
		# 	judulf = input("Judul: ")
		# 	jamt = input("Jam: ")
		# 	hargaf = input("Harga: ")
		# 	tiketf = input("Tiket: ")
		# 	bioskop = s.tambahfilm(ss,judulf,jamt,hargaf,tiketf)
	print("----------------------------")