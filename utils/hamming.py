import math

def obtenerCantidad ( mensaje:bin ):
    cantidad = 1
    for i in range(len(mensaje)):
        if pow(2, cantidad) >= cantidad + len(mensaje) + 1:
            return cantidad
        cantidad+=1
    return 0

def obtenerLista ( string:str ):
    listaString = []
    for i in string:
        listaString.append(i)
    return listaString

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
            if bin(i+1)[len(bin(i+1))-(j+1)] == '1':
                listaPrueba.append(mensajeParidad[i])
                
        if ( listaPrueba.count('0') % 2 != 0 ):
            listaPrueba[0] = '0'
        
        if ( listaPrueba.count('1') % 2 != 0 ):
            listaPrueba[0] = '1'    

        #print(listaPrueba)
        listaMensajeParidad[listaMensajeParidad.index('a')] = listaPrueba[0]
        listaPrueba.clear()
    
    return ''.join(listaMensajeParidad)

def obtenerParidadMensaje ( mensaje:bin ):
    mensajeOg = ""
    listaBitsParidad = []    

    for i in range ( len(mensaje) ):
        if ( i+1 == 1 or (math.log2(i+1).is_integer() and math.log2(i+1) != 0 )):
            listaBitsParidad.append(mensaje[i])
        else:
            mensajeOg += mensaje[i]
    
    return ''.join(listaBitsParidad), mensajeOg

def comprobarMensajeOg ( mensaje:bin):
    paridad, mensajeRecibido = obtenerParidadMensaje ( mensaje )
    calculadoRecibido = obtenerMensajeEnviar ( mensajeRecibido )
    paridadCalculado =  obtenerLista ( obtenerParidadMensaje ( calculadoRecibido )[0] )
    paridadCalculado[0]='0'
    paridadCalculado[3]='1'
    print(paridadCalculado)
    flag = True
    for i in range ( len(paridadCalculado) ):
        paridadCalculado[i] = str( int(paridadCalculado[i],2) ^ int(paridad[i],2) )
    posicionError = int(''.join(paridadCalculado),2)
    listaMensajeCorregido = []

    if ( posicionError > 0 and posicionError < 11):
        for i in mensaje:
            listaMensajeCorregido.append(i)
        listaMensajeCorregido[posicionError-1] = str ( int(listaMensajeCorregido[posicionError-1]) ^ 1 )
        flag = False

    return mensaje, flag, ''.join(listaMensajeCorregido)

def prueba():
    mensaje = '0110101'
    print(f"Mensaje original: {mensaje}")
    mensajeEnviado = obtenerMensajeEnviar(mensaje)
    print(f"Mensaje enviado: {mensajeEnviado}")
    print("--------------------")
    mensajeRecibido = comprobarMensajeOg(mensajeEnviado)
    print(f"Mensaje Recibido: {mensajeRecibido[0]}, ¿Llegó correcto? {mensajeRecibido[1]}, Corrección {mensajeRecibido[2]}")

if __name__ == '__main__':
    prueba()