import socket
import struct
import sys

multicast_group = "224.0.0.1"
server_address = ('', 5000)

# creamos el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# escuchamos en el puerto
sock.bind(server_address)

# tenemos que establecer el grupo de multicast sobre nuestras interfaces de red
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

# bucle de escucha/respuesta de peticiones

while True:
    print("Esperando una petición")
    data, direccion = sock.recvfrom(1024)
    print(f"Recibidos {len(data)} desde {direccion}")
    print(data.decode())
    print(f"Mandando comprobación de recibimiento a {direccion}")
    sock.sendto(b"ACK", direccion)