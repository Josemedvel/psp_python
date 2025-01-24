import socket
import json
import sys
import threading

def main():
    if len(sys.argv) < 2:
        print("No se ha especificado un nombre de archivo a solicitar")
        sys.exit(0)
    
    # cada archivo especificado se intenta descargar en un nuevo hilo cliente
    for file in sys.argv[1:]:
        threading.Thread(target=descargar_archivo, args=(file,)).start()



def descargar_archivo(nombre_archivo):
    direccion_server = ("localhost", 5000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect(direccion_server) # conectamos al server
    except TimeoutError as e:
        print(e)
        return

    print("Conexión establecida")
    json_nombre = json.dumps({"nombre": nombre_archivo}).encode()
    sock.sendall(json_nombre)
    
    metadatos = sock.recv(1024)
    if not metadatos:
        print(f"Ha habido un error leyendo los metadatos del archivo:{nombre_archivo}")
        return
    else:
        size = 1024
        metadatos_json = json.loads(metadatos)
        print(metadatos_json)
        if "error" in metadatos_json.keys():
            print(metadatos["error"])
            sock.close()
            return
        else:
            size = metadatos_json["size"]

        with open(nombre_archivo, "wb") as file:
            written = 0
            # hay que ir escribiendo todo el fichero en nuestro directorio de cliente
            while written < size:
                paquete = sock.recv(2048) # estos paquetes son puramente de datos
                if not paquete:
                    return
                file.write(paquete)
                written = written + len(paquete)
        print(f"Archivo {nombre_archivo} recibido correctamente")


if __name__ == "__main__":
    main()