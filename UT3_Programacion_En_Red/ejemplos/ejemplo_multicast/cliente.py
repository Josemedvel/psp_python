import socket
import struct
import sys

mensaje = "Información muy importante".encode()
multicast_group = ('224.0.0.1', 5000)

# Creamos el socket UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# establecemos un timeout para que no se quede bloqueado por siempre intentando recibir respuesta
sock.settimeout(0.2)

# establecemos el número de saltos, como va a ser un programa "local", pondremos 1
ttl = struct.pack('b', 6)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# ahora solo queda enviar la información como haríamos en un socket UDP normal y esperar respuesta
try:
    print(f"Enviando '{mensaje.decode()}'")
    enviado = sock.sendto(mensaje, multicast_group)

    # esperamos respuestas
    while True:
        print("Esperando respuesta")
        try:
            data, server = sock.recvfrom(1024)
        except socket.timeout:
            print("Cuenta atras terminada, no hay más respuestas")
            break
        else:
            print("Recibido {!r} from {}".format(data, server))
finally:
    print("Cerrando socket!")
    sock.close()