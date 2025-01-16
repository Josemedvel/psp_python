import socket
import threading

def responder_cliente(cliente, direccion):
    try:
        print(f"Conexión establecida con {direccion}")
        while True:
            data = cliente.recv(1024).decode()
            #print(data)
            if not data:
                break
            print(f"Mensaje recibido de {direccion}: {data}")
            # time.sleep(1)
            cliente.send(data.encode())
    except Exception as e:
        print(f"Error con el cliente: {e}")
    finally:
        cliente.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creamos el socket TCP
    direccion_server = ("127.0.0.1", 3000)
    server.bind(direccion_server)
    
    server.listen(5)
    print("Servidor escuchando en", direccion_server)

    while True:
        cliente, direccion_cliente = server.accept()
        hilo = threading.Thread(target=responder_cliente, args=(cliente, direccion_cliente))
        hilo.start()

if __name__ == "__main__":
    main()