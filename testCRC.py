from utils import crc
from utils import binario

#RECEPTOR (EL QUE RECIBE EL MENSAJE, SERVIDOR)
i = 2
nbits = '16'
gradoCRC = '64'
print(crc.polinomios['4'])
while True:
    if (int('0b' + ''.join(map(str,binario.getTestList(nbits)[i])),2) == int(crc.polinomios[gradoCRC],2)):
        i+=1
    
    mensajeOriginal = '0b' + ''.join(map(str,binario.getTestList(nbits)[i]))
    

    #EMISOR (EL QUE ENVIA EL MENSAJE, CLIENTE)
    mensajeEnviado = crc.getEnvio(mensajeOriginal, gradoCRC)
    
    mensajeRecibido = crc.obtenerMensajeOG(mensajeEnviado, gradoCRC)
    i+=1
    if(mensajeRecibido[2] == False):
        print(f"MENSAJE ORIGINAL:{mensajeOriginal}")
        print(f"MENSAJE ENVIADO: {mensajeEnviado}")
        print(f"MENSAJE RECIBIDO: {mensajeRecibido[0]}  CALCULADO: {mensajeRecibido[1]}  LLEGO CORRECTO: {mensajeRecibido[2]}")
        break;
    if (i == len(binario.getTestList(nbits))):
        print("TEST TERMINADO TODO BIEN")
        break;