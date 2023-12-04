'''
CLASE UTILIZADA PARA PROBAR LA CONEXION COMO CLIENTE
'''


from utils import conexion
from utils import crc
from utils import binario

ip = input('INGRESA LA IP')
mensaje = "ola"
mensaje_binario = '0b' + binario.toBin(mensaje)
print(mensaje_binario)
conexion.startClient(crc.getEnvio(mensaje_binario, '32'), ip)