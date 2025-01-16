import socket


direccion_servidor = ("127.0.0.1", 3000)
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect(direccion_servidor)
except Exception as e:
    print(f"Error: {e}")
    exit()
    
while True:
    try:
        while True:
            mensaje = input("Introduce un mensaje: ")
            if mensaje == "exit" or mensaje=="":
                break
            socket.send(mensaje.encode())
            respuesta = socket.recv(1024).decode()
            print(f"Respuesta del servidor: {respuesta}")
    except Exception as e:
        print(f"Error: {e}")
        break
    finally:
        socket.close()
        break