import paho.mqtt.client as mqtt
import time
import random
import json

BROKER = "node02.myqtthub.com"
PORT = 1883
USERNAME = "appsensores"
PASSWORD = "1234"
PUBLISH_TOPIC = "/temp"


print("Inicio programa")

# función que simula la lectura de datos de temperatura de un sensor
def publicar_datos():
    while True:
        dato_nuevo = random.uniform(15, 17)
        client.publish(PUBLISH_TOPIC, json.dumps({"temp": dato_nuevo},))
        time.sleep(10)


# función callback que se llamará cuando el cliente recibe un CONNACK (recibo de conexión exitosa) del servidor
def on_connect(client, userdata, flags, rc, properties):
    print(f"Conectado con código: {rc}")
    # nos suscribimos a los topics que queramos del servidor
    client.subscribe(PUBLISH_TOPIC)

# función de callback que se llama cuando se recibe un mensaje de PUBLISH desde el servidor
def on_message(client, userdata, msg):
    print(f"msg topic: {msg.topic}, datos: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "appsensores")
client.on_connect = on_connect
client.on_message = on_message

if USERNAME and PASSWORD:
    client.username_pw_set(username=USERNAME, password=PASSWORD)

try:
    print(f"Conectando al broker {BROKER}:{PORT}...")
    client.connect(BROKER, PORT, keepalive=60)
except Exception as e:
    print(f"No se pudo conectar al broker. Error: {e}")
    exit(1)

# Iniciar el bucle del cliente
try:
    client.loop_start() # inicia un bucle de escucha infinito en un hilo aparte
    publicar_datos()
except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
    client.disconnect()
    print("Cliente MQTT desconectado.")