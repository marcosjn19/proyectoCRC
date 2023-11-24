from itertools import product
def toBin ( msg: str ) -> str:
    cat = ''
    for i in msg:
        cat += bin(ord(i))[2::]
    return cat

def toPureBin ( msg: str ) -> int:
    cat = ""
    for i in msg:
        cat += bin(ord(i))[2::]
    return int(cat,2)

def fromBin ( cadena_binaria:str) -> str:
    # Divide la cadena binaria en bloques de 8 bits
    bloques_de_8_bits = [cadena_binaria[i:i+8] for i in range(0, len(cadena_binaria), 8)]

    # Convierte cada bloque de 8 bits a un número entero
    numeros_enteros = [int(bloque, 2) for bloque in bloques_de_8_bits]

    # Convierte los números enteros a caracteres ASCII y los une en una cadena
    cadena_ascii = ''.join(chr(numero) for numero in numeros_enteros)

    return cadena_ascii

def eraseType ( msg : str ) -> str:
    return msg[2::]

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

def getTestList(nbits:str):
    bits = [0, 1]
    return list(product(bits, repeat=int(nbits)))

def prueba():
    print('prueba')

if __name__ == '__main__':
    prueba()