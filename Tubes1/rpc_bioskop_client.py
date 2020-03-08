import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.1.4:8000')

i = 1
while (i != 0):
	bioskop = s.ambilfilm()
	print("XXI")
	print("Film yang tersedia:")
	for i in range(len(bioskop)):
		if (bioskop[i][4] != 0):
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
					if (y <= bioskop[i][4]):
						# jumlahtiket = bioskop[i][4]-y
						hargatotal = s.totalharga(bioskop[i][3],y)
						bioskop[i][4] = s.updatetiket(bioskop[i][1],bioskop[i][4],y)
						transaksi = s.simpantransaksi(bioskop[i][1],y,hargatotal)
						print("Harga yang harus dibayar ",hargatotal)
					else:
						print("Tiket tidak tersedia")
	print("--------------------")