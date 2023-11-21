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

def prueba():
    print('prueba')

if __name__ == '__main__':
    prueba()