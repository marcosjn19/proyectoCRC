import socket
def obtener_ip():
    try:
        # Crear un socket UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Conectar a un servidor DNS (puede ser cualquier dirección IP válida)
        ip = s.getsockname()[0]
        s.close()
        print(ip)
        return ip
    except socket.error:
        return "127.0.0.1"  # En caso de error, usar localhost

def setupServer():
    ip = obtener_ip()
    return [ip, 30900]

def startServer():
    data = setupServer()
    host = data[0]
    puerto = data[1]
    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # Enlace del socket al host y puerto
        servidor.bind((host, puerto))

        # Escuchar conexiones entrantes (hasta 1 conexión en este ejemplo)
        servidor.listen(1)
        print(f'Esperando conexiones en el puerto {puerto}...')

        # Aceptar la conexión
        conexion, direccion_cliente = servidor.accept()
        print(f'Conexión desde {direccion_cliente}')

        # Recibir y mostrar datos del cliente
        datos = conexion.recv(1024)
        print(f'Datos recibidos: {datos.decode()}')

def startClient(mensaje, ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((ip, 30900))
        mensaje = 'Hola mundo'
        cliente.sendall(mensaje.encode())
