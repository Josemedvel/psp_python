import socket
import json
import threading
import os

direccion_server = ("localhost", 5000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(direccion_server)

server.listen(5)

def listar(cliente, direccion):
    resultado_raw = os.listdir(".")
    resultado_clean  = []
    for x in resultado_raw:
        if x.startswith("test"):
            resultado_clean.append(x)
    if len(resultado_clean) == 0:
        mensaje = json.dumps({"error":"No hay tests"})
    else:
        mensaje = json.dumps({"tests":resultado_clean})
    cliente.send(mensaje.encode())


def acciones(cliente, direccion):
    data = cliente.recv(1024)
    if not data:
        cliente.close()
        print("la conexión se ha cerrado")
        return
    data_json = json.loads(data)
    print(data_json)
    match data_json["action"]:
        case "listar":
            listar(cliente, direccion)
        case _:
            pass

while True:
    cliente, direccion = server.accept()
    threading.Thread(target=acciones, args=(cliente, direccion)).start()


