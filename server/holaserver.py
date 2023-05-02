import socket
import time

# Configuración del servidor
host = 'localhost'
port = 9999

# Crear un objeto socket TCP/IP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de la dirección y el puerto del servidor
servidor.bind((host, port))

# Espera por conexiones entrantes
servidor.listen()

print(f"Servidor TCP/IP escuchando en {host}:{port}...")

# Bucle infinito para aceptar conexiones
while True:
    # Aceptar una nueva conexión
    conexion, direccion = servidor.accept()

    print(f"Conexión establecida desde {direccion[0]}:{direccion[1]}")

    # Enviar una palabra en mayúsculas cada 0.5 segundos
    while True:
        palabra = "HOLA"
        conexion.sendall(palabra.encode())
        time.sleep(0.5)
