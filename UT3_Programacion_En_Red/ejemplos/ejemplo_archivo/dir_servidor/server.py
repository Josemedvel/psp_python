import socket
import json
import threading
import os


def enviar_archivo(cliente: socket.SocketIO, direccion):
    paquete_nombre_fichero = cliente.recv(1024)
    if not paquete_nombre_fichero:
        print("Ha habido un error al recibir el nombre del archivo")
        cliente.close()
        return
    json_nombre = json.loads(paquete_nombre_fichero)
    if json_nombre["nombre"] == None:
        print("No existe la propiedad nombre en el json")
        print(json_nombre)
        return
    nombre_fichero = json_nombre["nombre"]

    if nombre_fichero not in os.listdir("."):
        print(f"No existe el archivo {nombre_fichero} en el servidor")
        metadatos = json.dumps({"error": f"No existe el archivo {nombre_fichero} en el servidor"})
        cliente.sendall(metadatos.encode())
        cliente.close()
        return

    print(f"Se procede a enviar el archivo {json_nombre['nombre']}")
    
    # extracción de la longitud
    with open(nombre_fichero, "rb") as file:
        size = len(file.read())
        metadatos = json.dumps({"size": size})
        cliente.sendall(metadatos.encode())
    with open(nombre_fichero, "rb") as file:
        while True:
            datos = file.read(2048)
            if not datos: # no queda nada
                break
            cliente.sendall(datos)
    print(f"Archivo '{nombre_fichero}' enviado al cliente '{direccion}'")
    # cerramos la conexión
    cliente.close()


def main():
    direccion_server = ("localhost", 5000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(direccion_server)
    sock.listen(10)
    print(f"Servidor iniciado en {direccion_server}")
    while True:
        (cliente, direccion) = sock.accept()
        threading.Thread(target=enviar_archivo, args=(cliente,direccion)).start()

if __name__ == "__main__":
    main()