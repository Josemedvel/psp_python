import json
import socket
import threading
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

direccion_server = ("localhost", 5000)

sock.connect(direccion_server)

mensaje = json.dumps({"action": "listar"})

sock.send(mensaje.encode())
data = sock.recv(1024)
if not data:
    sock.close()
    sys.exit()
data_json = json.loads(data)

if "error" in data_json:
    print(data_json["error"])
else:
    print(data_json["tests"])