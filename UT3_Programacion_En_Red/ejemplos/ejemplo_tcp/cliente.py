import socket
import json

direccion_server = ("127.0.0.1", 3000)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket TCP
cliente.connect(direccion_server)
print("conectado al servidor")

respuesta = json.loads(cliente.recv(1024)) # se queda esperando a la respuesta

print(f"Respuesta del servidor: {respuesta['nombre'].upper()} {respuesta['clase']}")

cliente.close()