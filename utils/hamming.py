import math

def obtenerCantidad ( mensaje:bin ):
    cantidad = 1
    for i in range(len(mensaje)):
        if pow(2, cantidad) >= cantidad + len(mensaje) + 1:
            return cantidad
        cantidad+=1
    return 0

def asignarParidad ( mensaje: bin ):
    mensajeParidad = len(mensaje)*'0' + obtenerCantidad(mensaje)*'0'
    listaMensajeOriginal = []
    listaMensaje = []

    for i in mensaje:
        listaMensajeOriginal.append(i)

    listaMensajeOriginal.reverse()

    for i in mensajeParidad:
        listaMensaje.append(i)

    for i in range ( len(listaMensaje) ):
        if ( i+1 == 1 or (math.log2(i+1).is_integer() and math.log2(i+1) != 0 )):
            listaMensaje[i] = 'a'
        else:
            listaMensaje[i] = listaMensajeOriginal.pop()

    return ''.join(listaMensaje)

def obtenerMensajeEnviar ( mensaje: bin ):
    mensajeParidad = asignarParidad(mensaje)
    listaMensajeParidad = []
    for i in mensajeParidad:
        listaMensajeParidad.append(i)
    listaPrueba = []
    for j in range(obtenerCantidad(mensaje)):
        for i in range(len(mensajeParidad)):
            #print(bin(i+1))
            if bin(i+1)[len(bin(i+1))-(j+1)] == '1':
                listaPrueba.append(mensajeParidad[i])
                
        
        if ( listaPrueba.count('0') % 2 != 0 ):
            listaPrueba[0] = '0'
        
        if ( listaPrueba.count('1') % 2 != 0 ):
            listaPrueba[0] = '1'    

        print(listaPrueba)
        listaMensajeParidad[listaMensajeParidad.index('a')] = listaPrueba[0]
        listaPrueba.clear()
    
    return ''.join(listaMensajeParidad)

def prueba():
    mensaje = '1001001010'
    print(obtenerCantidad(mensaje))
    print(obtenerMensajeEnviar(mensaje))

if __name__ == '__main__':
    prueba()