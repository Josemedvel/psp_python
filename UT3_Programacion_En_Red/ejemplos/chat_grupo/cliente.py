import socket
import json
import threading
import os
import hashlib


PORT = 3000
SERVER_ADDR = "localhost"

# devuelve un socket UDP
def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def read(user:str, sock: socket.SocketIO):
    while True:
        try:
            message, direccion = sock.recvfrom(1024)
            if not message:
                print("Error en el mensaje")
            else:
                message_json = json.loads(message)
                if message_json["user"] != user:
                    print(f"\r{message_json['user']}:{message_json['content']}")

        except Exception as e:
            print(f"Error leyendo: {e}")

def write(user, addr, sock):
    first_message = json.dumps({"user":user,"connect": f"{user}_connect"}).encode()
    sock.sendto(first_message, addr)
    while True:
        text = ""
        while text == "":
            text = input(f"{user}:\t")
        if text == "q":
            message = json.dumps({"user": user, "content" : "Se ha desconectado"}).encode()
        else:
            message = json.dumps({"user": user, "content": text}).encode()
        sock.sendto(message, addr)
        if text == "q":
            os._exit(0)

def main():
    sock = create_socket()
    user = input("Ingresa tu nombre de usuario:\t")
    threading.Thread(target=read, args=(user, sock)).start()
    threading.Thread(target=write, args=(user, (SERVER_ADDR, PORT), sock)).start()

if __name__ == "__main__":
    main()

