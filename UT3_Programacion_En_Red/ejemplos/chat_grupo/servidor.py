import socket
import json
import os

connected_clients = []

# devuelve un servidor UDP
def create_server(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((address, port))
    print(f"Servidor creado en {address}:{port}")
    return sock

def read(sock: socket.SocketIO):
    global connected_clients
    try:
        message, client_address = sock.recvfrom(1024)
        if not message:
            return None
        elif not is_client(client_address, connected_clients):
            connected_clients.append(client_address)
            return None
    except Exception as e:
        print(f"Error leyendo del socket: {e}")
    return message.decode()

def write(sock: socket.SocketIO, message: str):
    global connected_clients
    message_json = json.loads(message)
    if message_json["connect"] in message_json:
        return
    for addr in connected_clients:
        try:
            sock.sendto(message.encode(), addr)
        except Exception as e:
            print(f"Error enviando a {addr}: {e}")

def is_client(address, client_list):
    return address in client_list

def main():
    sock = create_server("localhost", 3000)
    while True:
        message = read(sock)
        print(message)
        if message:
            write(sock, message)

if __name__ == "__main__":
    main()