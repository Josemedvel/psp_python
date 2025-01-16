import socket
import sys


if len(sys.argv) != 2:
    exit()

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion_server = ('127.0.0.1', 3000)

socket.sendto(sys.argv[1].encode(), direccion_server)
data, address = socket.recvfrom(1024) # esperamos la respuesta del server
try:
    print(f"Recibido {int(data.decode())} de {address}")
except Exception as e:
    print(f"Recibido {data} de {address}")
    print(f"Error: {e}")