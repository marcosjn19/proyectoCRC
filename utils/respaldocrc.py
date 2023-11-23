global polinomioGenerador 
polinomioGenerador = 0
import binario
polinomios = {
    '3':'0b1101',
    '4':'0b10011',  #Polinomio CRC-4   -> 4bits
    '8':'0b100000111', #Polinomio CRC-8 -> 8bits
    '12':'0b1100000001111', #Polinomio CRC-12 -> 12bits
    '16':'0b11000000000000101', #Polinomio CRC-16 -> 16bits
    '32':'0b100110000010001110110110111', #Polinomio CRC-32 -> 32bits
    '64':'0b100001011110000111000011110101110101001111010100011011010010011' #Polinomio CRC-64 -> 64bits
}

def residuo ( mensaje, gradoPolinomio ):
    valores_ascii = binario.toPureBin(mensaje)
    valores_ascii = valores_ascii << int(gradoPolinomio)
    int_polinomio = int(polinomios[gradoPolinomio],2)
    resultado = valores_ascii % int_polinomio
    return(bin(resultado)[2::])

def residuoBin ( mensaje: bin, gradoPolinomio ):
    mensaje = int(mensaje,2)<<int(gradoPolinomio)
    int_polinomio = int(polinomios[gradoPolinomio],2)
    resultado = mensaje % int_polinomio
    return(bin(resultado)[2::])

def crearEnvio ( mensaje, gradoPolinomio):
    residuo = residuoBin(mensaje, gradoPolinomio)
    mensajeRes = mensaje + residuo
    if ( len(mensaje) != ( len(mensajeRes) - int(gradoPolinomio) ) ):
        for i in range ( len(mensajeRes) - len(mensaje) - 1 ):
            mensajeRes += '0'
    return mensajeRes

def getEnvio ( mensaje, gradoPolinomio ):
    residuo = residuoBin(mensaje, gradoPolinomio )
    mensajeBin = (int(mensaje,2)<<int(gradoPolinomio)) + int(residuoBin(mensaje,gradoPolinomio),2)
    return bin(mensajeBin)

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


'''mensaje = '0b1100'
print(residuoBin(mensaje,'3'))
print (mensaje)
mensajeBin = (int(mensaje,2)<<int('3')) + int(residuoBin(mensaje,'3'),2)
print(bin(mensajeBin))'''
mensajeOriginal = '0b1010'
print(f"MENSAJE ORIGINAL:{mensajeOriginal}")

#EMISOR (EL QUE ENVIA EL MENSAJE, CLIENTE)
mensajeEnviado = getEnvio(mensajeOriginal, '3')
print(f"MENSAJE ENVIADO: {mensajeEnviado}")

#RECEPTOR (EL QUE RECIBE EL MENSAJE, SERVIDOR)
mensajeRecibido = obtenerMensajeOG(mensajeEnviado,'3')
print(f"MENSAJE RECIBIDO: {mensajeRecibido[0]}  CALCULADO: {mensajeRecibido[1]}  LLEGO CORRECTO: {mensajeRecibido[2]}")