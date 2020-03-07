bioskop = []
studio1 = ['Studio 1', 'Yowes ben', '18.00-19.30', 30000, 50]
bioskop.append(studio1)
studio2 = ['Studio 2', 'Knives Out', '15.00-16.30', 50000, 20]
bioskop.append(studio2)
studio3 = ['Studio 3', 'Parasite', '12.00-13.30', 40000, 10]
bioskop.append(studio3)

i = 1
while (i != 0):
	print("XXI")
	print("Film yang tersedia:")
	for i in range(len(bioskop)):
		print(bioskop[i][1],' tayang pada pukul ',bioskop[i][2])
	print("-------------------")
	print("1. Pesan")
	print("0. Exit")
	i = int(input("Pilihan="))
	if (i == 1):
		film = input("Film yang dipilih=")
		for i in range(len(bioskop)):
			if (bioskop[i][1] == film) :
				print("Harga tiket ",bioskop[i][3])
				print("Sisa tiket yang tersedia ",bioskop[i][4])
				x = input("Beli/Tidak?[y/n]")
				if (x == 'y'):
					y = int(input("Banyaknya tiket="))
					bioskop[i][4] = bioskop[i][4]-y
					hargatotal = bioskop[i][3] * y
					print("Harga yang harus dibayar ",hargatotal)