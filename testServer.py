from utils import conexion
from utils import crc

datosRecibidos = conexion.startServer()
print(datosRecibidos)
mensajeRecibido = crc.obtenerMensajeOG(datosRecibidos, '32')
print(mensajeRecibido)