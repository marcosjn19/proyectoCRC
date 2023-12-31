'''
CLASE UTILIZADA COMO AUXILIAR PARA REALIZAR LA CORRECTA CONEXION ENTRE EMISOR
                    Y RECEPTOR
'''

import socket

#--------------------------------------------------------------------------
#METODO PARA OBTENER LA IP DEL QUE VA A RECIBIR
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

#--------------------------------------------------------------------------
#METODO AUXILIAR QUE REGRESA LA IP Y EL PUERTO (30900)
def setupServer():
    ip = obtener_ip()
    return [ip, 30900]

#--------------------------------------------------------------------------
#METODO PARA QUE EL SERVER COMIENZE A 'ESCUCHAR'
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
        return datos.decode()

#--------------------------------------------------------------------------
#METODO PARA QUE EL CLIENTE ENVIE EL MENSAJE
def startClient(mensaje, ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((ip, 30900))
        cliente.sendall(mensaje.encode())
