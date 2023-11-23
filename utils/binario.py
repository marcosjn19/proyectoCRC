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