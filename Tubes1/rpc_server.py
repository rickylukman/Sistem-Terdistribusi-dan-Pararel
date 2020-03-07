from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Operasi hitung
    def operasi_pangkat(x, y):
        return x ** y
    server.register_function(operasi_pangkat, 'pow')

    def operasi_tambah(x, y):
        return x + y
    server.register_function(operasi_tambah, 'add')

    def operasi_kali(x, y):
        return x * y
    server.register_function(operasi_kali, 'mul')

    def operasi_bagi(x, y):
        return x / y
    server.register_function(operasi_bagi, 'div')

    def operasi_kurang(x, y):
        return x - y
    server.register_function(operasi_kurang, 'sub')

    # Run the server's main loop
    server.serve_forever()