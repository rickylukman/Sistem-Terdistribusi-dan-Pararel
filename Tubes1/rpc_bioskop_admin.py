import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.1.4:8000')

i = 1
while (i != 0):
	print("Menu admin")
	print("1. Lihat transaksi")
	print("2. Edit Studio")
	print("0. Exit")
	i = int(input("Pilihan="))
	if (i == 1):
		transaksi = s.ambiltransaksi()
		for x in range(len(transaksi)):
			print(x+1, transaksi[x])
	elif (i == 2):
		bioskop = s.ambilfilm()
		for i in range(len(bioskop)):
			if (bioskop[i][4] != 0):
				print(bioskop[i][0], bioskop[i][1],' tayang pada pukul ',bioskop[i][2])
		print("Menu edit")
		print("1. Edit film studio 1")
		print("2. Edit film studio 2")
		print("3. Edit film studio 3")
		print("0. Kembali")
		n = int(input("Pilihan="))
		print("-----------------------------------------------")
		if (n != 0):
			studio = n-1
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
	print("----------------------------")