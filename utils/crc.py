global polinomioGenerador 
polinomioGenerador = 0

polinomios = {
    '3':'0b1101',
    '4':'0b10011',  #Polinomio CRC-4   -> 4bits
    '8':'0b100000111', #Polinomio CRC-8 -> 8bits
    '12':'0b1100000001111', #Polinomio CRC-12 -> 12bits
    '16':'0b11000000000000101', #Polinomio CRC-16 -> 16bits
    #'32':'0b100110000010001110110110111', #Polinomio CRC-32 -> 32bits
     '32':'0b100000100100000010000110110110101',
    '64':'0b10000000000000000000000000000000000000000000000000000000000011011' #Polinomio CRC-64 -> 64bits
}

def residuoBin ( mensaje: bin, gradoPolinomio ):
    mensaje = int(mensaje,2)<<int(gradoPolinomio)
    mensajeBits = bin(mensaje)[2::]
    sizeMensaje = len(mensajeBits)
    polinomio = polinomios[gradoPolinomio][2::]

    resultado = int(mensajeBits[0:int(gradoPolinomio)+1],2) ^ int(polinomio,2)
    resultado = bin(resultado)
    #print("Primer resultado: " + resultado)
    for i in range (int(gradoPolinomio)+1, sizeMensaje):
        if ( len(resultado)-2 == len(polinomio)):
            resultado = int(resultado,2) ^ int(polinomio,2)
            resultado = bin(resultado)
            #print(f"Resultado de la iteracion {i} = {resultado}")
        else:
            resultado += mensajeBits[i]
            #print(f"Resultado de la iteracion {i} = {resultado}")
            if ( len(resultado)-2 == len(polinomio)):
                resultado = int(resultado,2) ^ int(polinomio,2)
                resultado = bin(resultado)
                #print(f"Resultado de la iteracion {i} = {resultado}")

    return(resultado[2::])

def getEnvio ( mensaje, gradoPolinomio ):
    #mensajeBin = (int(mensaje,2)<<int(gradoPolinomio)) + int(residuoBin(mensaje,gradoPolinomio),2)
    residuo = residuoBin(mensaje,gradoPolinomio).zfill(int(gradoPolinomio))
    mensajeBin = mensaje + residuo
    return mensajeBin

#FUNCION PARA SACAR LOS N DIGITOS QUE SE SACARON DEL ^
def obtenerMensajeOG ( mensaje:bin, gradoPolinomio ):
    grado = int(gradoPolinomio)
    calculado = mensaje[len(mensaje)-int(gradoPolinomio)::]
    mensajeOG = int(mensaje,2) >> grado
    residuoC = residuoBin(bin(mensajeOG), gradoPolinomio)
    correcto = False
    if int(residuoC) == int(calculado):
        correcto = True
    return {0:bin(mensajeOG), 1:calculado, 2:correcto}

def prueba():
    #EMISOR (EL QUE ENVIA EL MENSAJE, CLIENTE)
    mensajeEnviado = getEnvio(mensajeOriginal, '4')
    print(f"MENSAJE ENVIADO: {mensajeEnviado}")

    #RECEPTOR (EL QUE RECIBE EL MENSAJE, SERVIDOR)
    mensajeRecibido = obtenerMensajeOG(mensajeEnviado,'4')
    print(f"MENSAJE RECIBIDO: {mensajeRecibido[0]}  CALCULADO: {mensajeRecibido[1]}  LLEGO CORRECTO: {mensajeRecibido[2]}")

if __name__ == '__main__':
    prueba()

mensajeOriginal = '0b1101'
print(f"MENSAJE ORIGINAL:{mensajeOriginal}")

