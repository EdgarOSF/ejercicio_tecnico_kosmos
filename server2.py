import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)
sock.bind(server_address)

sock.listen(1)


sc, addr = sock.accept()

while True:
    recibido = sc.recv(1024)
    if not recibido:
        print("Cliente desconectado")
        break

    mensaje = recibido.decode()

    if mensaje.upper() == 'DESCONEXION':
        print(f"Cliente {addr} cerró sesión")
        break
    
    respuesta = mensaje.upper()

    sc.sendall(respuesta.encode())


sc.close()