global polinomioGenerador 
polinomioGenerador = 0
import binario
polinomios = {
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
    mensaje = mensaje<<int(gradoPolinomio)
    int_polinomio = int(polinomios[gradoPolinomio],2)
    resultado = mensaje % int_polinomio
    return(bin(resultado)[2::])

#FUNCION PARA SACAR LOS N DIGITOS QUE SE SACARON DEL ^
def obtenerMensajeOG ( mensaje:bin, gradoPolinomio ):
    grado = int(gradoPolinomio)
    mensajeOG = int(mensaje,2) >> grado
    return mensajeOG


mensaje = 'a'
print(residuo(mensaje,'16'))
mensajeBin = bin(binario.toPureBin(mensaje))
mensajeBin += residuo(mensaje,'16')
print(mensajeBin)
mensajeOG = obtenerMensajeOG(mensajeBin, '16')
print(mensajeOG)