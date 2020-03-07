import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Print semua operasi yang dapat dilakukan
print(s.system.listMethods())
print("--------------------")
#Eksekusi
x1 = int(input("Nilai x1 = "))
x2 = int(input("Nilai x2 = "))
print("x1 =",x1)
print("x2 =",x2)
print()
print("Pangkat : ",s.pow(x1,x2)) 
print("Tambah  : ",s.add(x1,x2)) 
print("Kali    : ",s.mul(x1,x2)) 
print("Bagi    : ",s.div(x1,x2)) 
print("Kurang  : ",s.sub(x1,x2)) 


#s.close()