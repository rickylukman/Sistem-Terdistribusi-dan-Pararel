bioskop = []
studio1 = ['Studio 1', 'Yowes ben', '18.00-19.30', 30000, 50]
bioskop.append(studio1)
studio2 = ['Studio 2', 'Knives Out', '15.00-16.30', 50000, 20]
bioskop.append(studio2)
studio3 = ['Studio 3', 'Parasite', '12.00-13.30', 40000, 10]
bioskop.append(studio3)

i = 1
while (i != 0):
	print("-----------------------------------------------")
	print("		XXI")
	print("	Film yang tersedia:")
	for i in range(len(bioskop)):
		if (bioskop[i][4] != 0):
			print(bioskop[i][1],' tayang pada pukul ',bioskop[i][2])
	print("-----------------------------------------------")
	print("Menu edit")
	print("1. Edit film studio 1")
	print("2. Edit film studio 2")
	print("3. Edit film studio 3")
	print("0. Exit")
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

# i = 1
# while (i != 0):
# 	print("XXI")
# 	print("Film yang tersedia:")
# 	for i in range(len(bioskop)):
# 		if (bioskop[i][4] != 0):
# 			print(bioskop[i][1],' tayang pada pukul ',bioskop[i][2])
# 	print("-------------------")
# 	print("1. Pesan")
# 	print("0. Exit")
# 	i = int(input("Pilihan="))
# 	if (i == 1):
# 		film = input("Film yang dipilih=")
# 		for i in range(len(bioskop)):
# 			if (bioskop[i][1] == film) :
# 				print("Harga tiket ",bioskop[i][3])
# 				print("Sisa tiket yang tersedia ",bioskop[i][4])
# 				x = input("Beli/Tidak?[y/n]")
# 				if (x == 'y'):
# 					y = int(input("Banyaknya tiket="))
# 					if (y <= bioskop[i][4]):
# 						bioskop[i][4] = bioskop[i][4]-y
# 						hargatotal = bioskop[i][3] * y
# 						print("Harga yang harus dibayar ",hargatotal)
# 					else:
# 						print("Tiket tidak tersedia")
# 	print("--------------------")