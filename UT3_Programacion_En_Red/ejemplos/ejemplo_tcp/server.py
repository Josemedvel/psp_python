import socket
import time
import json

direccion_server = ("localhost", 3000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(direccion_server)
server.listen(10) # escuchamos y encolamos 10 conexiones
print(f"Servidor escuchando en {direccion_server[0]}:{direccion_server[1]}")

while True:
    # Aceptamos la conexión
    socket_cliente, direccion_cliente = server.accept()
    #time.sleep(2) # tardamos en dar la respuesta
    info = json.dumps({"nombre": "Jose", "clase": "DAM"})
    socket_cliente.send(info.encode())
    socket_cliente.close()