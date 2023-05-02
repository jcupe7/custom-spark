import socket
import time

# Definir la dirección IP y el puerto del servidor
IP = '127.0.0.1'
PORT = 9999

# Crear un objeto socket para el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el objeto socket con la dirección IP y el puerto
server_socket.bind((IP, PORT))

# Esperar conexiones entrantes
server_socket.listen()

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f'Conexión entrante desde {client_address}')

    # Enviar el archivo .wav cada 3 segundos
    while True:
        try:
            with open('./audios/audio.wav', 'rb') as f:
                data = f.read()
                client_socket.sendall(data)
        except FileNotFoundError:
            print('El archivo .wav no se encuentra en la ruta especificada')
            break

        time.sleep(3)
