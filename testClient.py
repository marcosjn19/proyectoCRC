from utils import conexion
from utils import crc
from utils import binario

ip = input('INGRESA LA IP')
mensaje = "ola"
print( '0b' + binario.toBin(mensaje) )
conexion.startClient(crc.getEnvio(mensaje, '16'), ip)