'''
Este servidor responde siempre con un número aleatorio al cliente que se conecta.
'''
import socket
import random


direccion_server = ('127.0.0.1', 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(direccion_server)

print(f"Servidor escuchando en la dirección: {direccion_server[0]}:{direccion_server[1]}")

while(True):
    data, address = server.recvfrom(1024)
    numero = random.randint(1, 100)
    print(f"Recibido {data.decode()} de {address}")
    server.sendto(str(numero).encode(), address)