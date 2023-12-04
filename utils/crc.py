'''
CLASE UTILIZADA COMO AUXILIAR PARA EL PROCEDIMIENTO NECESARIO PARA APLICAR
            EL METODO DE CRC PARA DETECCION DE ERRORES
'''
#Declaramos como global el polinomio generador para poderlo utilizarlo en toda la clase
global polinomioGenerador 
polinomioGenerador = 0

#Polinomios que se utilizaran a lo largo del procedimiento
polinomios = {
    '3':'0b1101',
    '4':'0b10011',  #Polinomio CRC-4   -> 4bits
    '8':'0b100000111', #Polinomio CRC-8 -> 8bits
    '12':'0b1100000001111', #Polinomio CRC-12 -> 12bits
    '16':'0b11000000000000101', #Polinomio CRC-16 -> 16bits
    '32':'0b100000100100000010000110110110101',
    '64':'0b10000000000000000000000000000000000000000000000000000000000011011' #Polinomio CRC-64 -> 64bits
}

#--------------------------------------------------------------------------
#METODO PARA CALCULAR EL RESIDUO DE UN MENSAJE DADO EN BASE AL GRADO DEL POLINOMIO
def residuoBin ( mensaje: bin, gradoPolinomio ):
    #Hacemos un desplazamiento de bits a la izquierda de los n grados del polinomio a usar
    mensaje = int(mensaje,2)<<int(gradoPolinomio)
    #Le quitamos el '0b' al valor binario del mensaje
    mensajeBits = bin(mensaje)[2::]
    #Obtenemos su tamaño
    sizeMensaje = len(mensajeBits)
    #Le quitamos el '0b' al polinomio a utilizar
    polinomio = polinomios[gradoPolinomio][2::]

    #Comenzamos con el procedimiento para calcular el residuo de los xor consecutivos
    #Obtenemos un primer resultado tomando n bits (segun sea el grado del polinomio) y
    #les hacemos un xor con el polinomio
    resultado = int(mensajeBits[0:int(gradoPolinomio)+1],2) ^ int(polinomio,2)
    #representamos el resultado en un binario
    resultado = bin(resultado)
    #Con un for recorremos desde el grado del polinomio +1 hasta el tamaño del mensaje
    for i in range (int(gradoPolinomio)+1, sizeMensaje):
        #Si la longitud del resultado (le restamos 2 por el '0b') es igual a la del polinomio
        #calcula un nuevo resultado
        if ( len(resultado)-2 == len(polinomio)):
            resultado = int(resultado,2) ^ int(polinomio,2)
            resultado = bin(resultado)
            #print(f"Resultado de la iteracion {i} = {resultado}")
        else:
            #Si no es asi, añade el siguiente bit (el de la posicion i) a resultado
            resultado += mensajeBits[i]
            #print(f"Resultado de la iteracion {i} = {resultado}")
            #Y verificamos nuevamente si la longitud del resultado es igual a la del polinomio calcula un nuevo resultado
            if ( len(resultado)-2 == len(polinomio)):
                resultado = int(resultado,2) ^ int(polinomio,2)
                resultado = bin(resultado)
                #print(f"Resultado de la iteracion {i} = {resultado}")

    #Regresamos el resultado (nuestro residuo de los xor consecutivos)
    return(resultado[2::])

#--------------------------------------------------------------------------
#METODO PARA OBTENER EL MENSAJE A ENVIAR 
def getEnvio ( mensaje, gradoPolinomio ):
    #Calculamos el residuo con el metodo anterior y lo rellenamos de 0's segun sea el grado del polinomio
    #Esto con el fin de que por ejemplo, si el residuo es 1, le añada n 0's a la izquierda 0001
    residuo = residuoBin(mensaje,gradoPolinomio).zfill(int(gradoPolinomio))
    #Al mensaje le concatenamos el residuo
    mensajeBin = mensaje + residuo
    #Regresamos el mensaje con el residuo
    return mensajeBin

#--------------------------------------------------------------------------
#METODO PARA OBTENER EL MENSAJE ORIGINAL Y COMPROBAR SI LLEGO BIEN
def obtenerMensajeOG ( mensaje:bin, gradoPolinomio ):
    #Sacamos el grado del proporcionado por el usuario
    grado = int(gradoPolinomio)
    #Sacamos el CRC calculado del mensaje (las n ultimas posiciones dadas por el grado)
    calculado = mensaje[len(mensaje)-int(gradoPolinomio)::]
    #Obtenemos el mensaje recibido quitando el CRC
    mensajeOG = int(mensaje,2) >> grado
    #Obtenemos el CRC del mensaje recibido
    residuoC = residuoBin(bin(mensajeOG), gradoPolinomio)
    #Colocamos la bandera de correcto en falso
    correcto = False
    #Si el CRC del recibido es igual al calculado del mismo, correcto pasa a verdadero
    if int(residuoC) == int(calculado):
        correcto = True
    #Regresamos el mensaje recibido, su crc calculado y si llego correctamente
    return {0:bin(mensajeOG), 1:calculado, 2:correcto}

#--------------------------------------------------------------------------
#METODO PARA PROBAR EL CORRECTO FUNCIONAMIENTO
def prueba():
    mensajeOriginal = '0b1101'
    print(f"MENSAJE ORIGINAL:{mensajeOriginal}")
    #EMISOR (EL QUE ENVIA EL MENSAJE, CLIENTE)
    mensajeEnviado = getEnvio(mensajeOriginal, '4')
    print(f"MENSAJE ENVIADO: {mensajeEnviado}")

    #RECEPTOR (EL QUE RECIBE EL MENSAJE, SERVIDOR)
    mensajeRecibido = obtenerMensajeOG(mensajeEnviado,'4')
    print(f"MENSAJE RECIBIDO: {mensajeRecibido[0]}  CALCULADO: {mensajeRecibido[1]}  LLEGO CORRECTO: {mensajeRecibido[2]}")

if __name__ == '__main__':
    prueba()


