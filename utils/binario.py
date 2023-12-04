'''
CLASE UTILIZADA COMO AUXILIAR PARA CIERTAS UTILIDADES CON 
            BINARIOS
'''

from itertools import product

#--------------------------------------------------------------------------
#METODO PARA OBTENER EL BINARIO DE UN STRING EN FORMA DE STRING
def toBin ( msg: str ) -> str:
    cat = ''
    for i in msg:
        cat += bin(ord(i))[2::]
    return cat

#--------------------------------------------------------------------------
#METODO PARA OBTENER EL BINARIO DE UN STRING EN FORMA DE ENTERO
def toPureBin ( msg: str ) -> int:
    cat = ""
    for i in msg:
        cat += bin(ord(i))[2::]
    return int(cat,2)

#--------------------------------------------------------------------------
#METODO PARA OBTENER DE UN BINARIO SU CADENA EN ASCII
def fromBin ( cadena_binaria:str) -> str:
    # Divide la cadena binaria en bloques de 7 bits
    bloques_de_7_bits = [cadena_binaria[i:i+7] for i in range(0, len(cadena_binaria), 7)]

    # Convierte cada bloque de 7 bits a un número entero
    numeros_enteros = [int(bloque, 2) for bloque in bloques_de_7_bits]

    # Convierte los números enteros a caracteres ASCII y los une en una cadena
    cadena_ascii = ''.join(chr(numero) for numero in numeros_enteros)

    return cadena_ascii

#--------------------------------------------------------------------------
#METODO AUXILIAR PARA BORRAR EL '0b' DE UN BINARIO
def eraseType ( msg : str ) -> str:
    return msg[2::]

#--------------------------------------------------------------------------
#METODO AUXILIAR PARA OBTENER TODAS LAS COMBINACIONES DE UN NUMERO
#BINARIO DE 4 BITS
def getTestList4():
    bits = [0, 1]
    combinaciones = []

    for bit1 in bits:
        for bit2 in bits:
            for bit3 in bits:
                for bit4 in bits:
                    combinacion = [bit1, bit2, bit3, bit4]
                    combinaciones.append(combinacion)

    return combinaciones

#--------------------------------------------------------------------------
#METODO AUXILIAR PARA OBTENER TODAS LAS COMBINACIONES DE UN NUMERO
#BINARIO DE N BITS
def getTestList(nbits:str):
    bits = [0, 1]
    return list(product(bits, repeat=int(nbits)))

#--------------------------------------------------------------------------
#METODO PARA PROBAR
def prueba():
    print('prueba')

if __name__ == '__main__':
    prueba()