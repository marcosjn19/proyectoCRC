'''
CLASE UTILIZADA PARA REALIZAR PRUEBAS DE CASOS DE USO
         DEL METODO PROGRAMADO DEL CRC
'''

from utils import crc
from utils import binario

#RECEPTOR (EL QUE RECIBE EL MENSAJE, SERVIDOR)
i = 2
#Establecemos la cantidad de bits para las pruebas (maximo 12 -> Si son más, consume mas recursos)
nbits = '4'
#Establecemos el grado de CRC a probar
gradoCRC = '64'

#Hacemos las pruebas
while True:
    #Si la combinacion de bits es igual al polinomio usado, saltar este caso
    #(Se supone que esto no debe de suceder, el polinomio debe de tener mas bits que el mensaje)
    if (int('0b' + ''.join(map(str,binario.getTestList(nbits)[i])),2) == int(crc.polinomios[gradoCRC],2)):
        i+=1
    
    #Mensaje a enviar
    mensajeOriginal = '0b' + ''.join(map(str,binario.getTestList(nbits)[i]))
    
    #EMISOR (EL QUE ENVIA EL MENSAJE, CLIENTE)
    mensajeEnviado = crc.getEnvio(mensajeOriginal, gradoCRC)
    
    #RECEPTOR (mensjae recibido)
    mensajeRecibido = crc.obtenerMensajeOG(mensajeEnviado, gradoCRC)

    #aumentamos el indice
    i+=1
    #En caso de que un caso nos de en falso, mostrar cual fue (algo salió mal)
    if(mensajeRecibido[2] == False):
        print(f"MENSAJE ORIGINAL:{mensajeOriginal}")
        print(f"MENSAJE ENVIADO: {mensajeEnviado}")
        print(f"MENSAJE RECIBIDO: {mensajeRecibido[0]}  CALCULADO: {mensajeRecibido[1]}  LLEGO CORRECTO: {mensajeRecibido[2]}")
        break;
    #Si se recorrieron todos los indices sin errores, mostrar que todo estaba bien
    if (i == len(binario.getTestList(nbits))):
        print("TEST TERMINADO TODO BIEN")
        break;