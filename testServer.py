from utils import conexion
from utils import crc
from utils import binario

datosRecibidos = conexion.startServer()
print(datosRecibidos)
mensajeRecibido = crc.obtenerMensajeOG(datosRecibidos, '32')
print(mensajeRecibido)

print(binario.fromBin(mensajeRecibido[0][2::]))