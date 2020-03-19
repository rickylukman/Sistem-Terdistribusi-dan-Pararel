from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

#input data film untuk studio di bioskop
    bioskop = []
    studio1 = ['Studio 1', 'Yowes Ben', '18.00-19.30', 30000, 50]
    bioskop.append(studio1)
    studio2 = ['Studio 2', 'Knives Out', '15.00-16.30', 50000, 20]
    bioskop.append(studio2)
    studio3 = ['Studio 3', 'Parasite', '12.00-13.30', 40000, 10]
    bioskop.append(studio3)
    transaksi = []

#ambil isi informasi array bioskop keseluruhan
    def operasi_bioskop_ambil():
        return bioskop
    server.register_function(operasi_bioskop_ambil, 'ambilfilm')

#melakukan update jumlah tiket jika ada pembelian
    def operasi_bioskop_updatetiket(film,tiket,jumlahbeli):
        for i in range(len(bioskop)):
            if (bioskop[i][1] == film):
                bioskop[i][4] = tiket-jumlahbeli
                return bioskop[i][4]
    server.register_function(operasi_bioskop_updatetiket, 'updatetiket') 

#update informasi studio jika terjadi pembaharuan jam tayang, film, dll
    def operasi_bioskop_updatestudio(studio,film,jamtayang,harga,tiket):
        for i in range(len(bioskop)):
            if (bioskop[i][0] == studio):
                bioskop[i][1] = film
                bioskop[i][2] = jamtayang
                bioskop[i][3] = harga
                bioskop[i][4] = tiket
                return bioskop
    server.register_function(operasi_bioskop_updatestudio, 'updatestudio')

#menghitung total pembayaran harga tiket
    def operasi_total_harga(harga,jumlahbeli):
        hargatotal = harga * jumlahbeli
        return hargatotal
    server.register_function(operasi_total_harga, 'totalharga') 

#ambil informasi transaksi yang dilakukan
    def operasi_ambil_transaksi():
        return transaksi
    server.register_function(operasi_ambil_transaksi, 'ambiltransaksi')

#menyimpan history transaksi yang berhasil
    def operasi_simpan_transaksi(film,jumlahbeli,hargatotal):
        transaksiX = [film, jumlahbeli, hargatotal]
        transaksi.append(transaksiX)
        return transaksi
    server.register_function(operasi_simpan_transaksi, 'simpantransaksi')            

    # Run the server's main loop
    server.serve_forever()