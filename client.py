import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)
sock.connect(server_address)

try:
    while True:
        mensaje = input("Ingresa un mensaje: ")

        # Enviar mensaje al servidor
        sock.sendall(mensaje.encode())

        if mensaje.upper() == 'DESCONEXION':
            print("Desconectando del servidor...")
            break

        # Esperar respuesta del servidor
        respuesta = sock.recv(1024)
        print("Servidor:", respuesta.decode())

finally:
    sock.close()
    print("Conexión cerrada.")