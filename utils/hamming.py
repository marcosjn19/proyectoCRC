'''
CLASE UTILIZADA COMO AUXILIAR PARA EL PROCEDIMIENTO NECESARIO PARA APLICAR
                    EL METODO DE DISTANCIA HAMMING
'''

import math

#--------------------------------------------------------------------------
#METODO PARA OBTENER LA CANTIDAD DE BITS DE PARIDAD BAJO LA REGLA
#                        2^p >= p + i + 1
def obtenerCantidad ( mensaje:bin ):
    cantidad = 1
    #Ciclo para ir revisando la cantidad de bits bajo la regla de arriba
    for i in range ( len ( mensaje ) ):
        #Si se aplica bien la regla, regresa la  cantidad
        if pow( 2, cantidad ) >= cantidad + len(mensaje) + 1:
            return cantidad
        #De no ser asi continua sumando
        cantidad += 1
    return 0

#--------------------------------------------------------------------------
#METODO AUXILIAR PARA OBTENER UNA LISTA DE UN STRING DADO
def obtenerLista ( string:str ):
    listaString = []
    for i in string:
        listaString.append(i)
    return listaString

#--------------------------------------------------------------------------
#METODO PARA ASIGNAR LOS BITS DE PARIDAD DADO UN MENSAJE EN BINARIO

def asignarParidad ( mensaje: bin ):
    #Se le añaden los bits dados por la cantidad de bits de paridad
    mensajeParidad = len(mensaje)*'0' + obtenerCantidad(mensaje)*'0'

    listaMensajeOriginal = []
    listaMensaje = []

    #Ponemos los caracteres del mensaje en una lista
    for i in mensaje:
        listaMensajeOriginal.append(i)

    #Invertimos la lista, para que los bits sean de izquierda a derecha
    listaMensajeOriginal.reverse()

    for i in mensajeParidad:
        listaMensaje.append(i)

    #Vamos añadiendo los bits de paridad, en este caso los representamos con una 'a'
    for i in range ( len(listaMensaje) ):
            #Primera posición siempre tiene paridad ó la posición es una potencia de 2 y no es 1
        if ( i+1 == 1 or (math.log2(i+1).is_integer() and math.log2(i+1) != 0 )):
            listaMensaje[i] = 'a'
        else:
            #Si no es un bit de paridad, va añadiendo de la lista del mensajeOriginal
            listaMensaje[i] = listaMensajeOriginal.pop()

    #Regresa en forma de string el mensaje con los bits de paridad con 'a'
    return ''.join(listaMensaje)


#--------------------------------------------------------------------------
#METODO PARA OBTENER EL MENSAJE A ENVIAR
def obtenerMensajeEnviar ( mensaje: bin ):
    #asignamos los bits de paridad en base al mensaje dado
    mensajeParidad = asignarParidad(mensaje)
    listaMensajeParidad = []
    #Lo colocamos en una lista
    for i in mensajeParidad:
        listaMensajeParidad.append(i)

    #Creamos una lista auxiliar    
    listaPrueba = []
    #Vamos realizando el proceso de ir "bajando" los bits
    #              Cantidad de bits de paridad (4)
    for j in range ( obtenerCantidad(mensaje) ):
                        #longitud de mensajeParidad
        for i in range ( len(mensajeParidad) ):
            #Si el binario de la posición (i+1) contiene en la posición longitud - (j+1) (Esto porque vamos de derecha a izquierda) 
            # es un '1' se "baja" el bit (en este caso se asigna a la lista auxiliar)
            if bin(i+1)[len(bin(i+1))-(j+1)] == '1':
                listaPrueba.append(mensajeParidad[i])

        #Si la cantidad de 0's es la impar, el bit de paridad es un 0        
        if ( listaPrueba.count('0') % 2 != 0 ):
            listaPrueba[0] = '0'
        
        #Si la cantidad de 1's es la impar, el bit de paridad es un 1
        if ( listaPrueba.count('1') % 2 != 0 ):
            listaPrueba[0] = '1'    

        #Asignamos el bit de paridad donde este el proximo index de 'a'
        listaMensajeParidad[listaMensajeParidad.index('a')] = listaPrueba[0]

        #Reseteamos la lista auxiliar
        listaPrueba.clear()
    #Regresamos la lista del mensaje con los bits de paridad como un str
    return ''.join(listaMensajeParidad)

#--------------------------------------------------------------------------
#METODO PARA OBTENER LOS BITS DE PARIDAD Y EL MENSAJE RECIBIDO
def obtenerParidadMensaje ( mensaje:bin ):
    mensajeOg = ""
    listaBitsParidad = []    
    #Separaremos los bits de paridad del mensaje recibido con la misma lógica que
    #se asignaron
    for i in range ( len(mensaje) ):
        #Primera posición siempre tiene paridad ó la posición es una potencia de 2 y no es 1
        if ( i+1 == 1 or (math.log2(i+1).is_integer() and math.log2(i+1) != 0 )):
            listaBitsParidad.append(mensaje[i])
        else:
            #Recuperamos el bit que es del mensaje
            mensajeOg += mensaje[i]
    
    #Regresamos dos elementos, el str de los bits de paridad y el mensaje recibido
    return ''.join(listaBitsParidad), mensajeOg

#--------------------------------------------------------------------------
#METODO PARA COMPROBAR Y CORREGIR (de ser necesario) EL MENSAJE RECIBIDO
def comprobarMensajeOg ( mensaje:bin):
    #Utilizamos el metodo anterior a este para poder obtener los bits de paridad y el mensaje recibido
    #mensaje = mensaje[:1]+'0'+mensaje[2:] #<- Simular un fallo
    paridad, mensajeRecibido = obtenerParidadMensaje ( mensaje )
    #Utilizamos los metodos que ya tenemos para calcular los bits de paridad del mensaje recibido
                        #Obtenemos un "mensaje a enviar" del recibido
    calculadoRecibido = obtenerMensajeEnviar ( mensajeRecibido )
    #Obtenemos solamente los bits de paridad del recibido
    paridadCalculado =  obtenerLista ( obtenerParidadMensaje ( calculadoRecibido )[0] )

    '''
    Para probar que funcione la corrección de errores:
    #paridadCalculado[0]='0'
    #paridadCalculado[3]='1'
    #print(paridadCalculado)
    '''
    #Bandera para decir si llego bien o no el mensaje
    flag = True
    #Hacemos un xor de los bits de paridad que llegaron con el mensaje y los calculados del mismo
    for i in range ( len(paridadCalculado) ):
        paridadCalculado[i] = str( int(paridadCalculado[i],2) ^ int(paridad[i],2) )
    
    #Obtenemos la posición del error convirtiendo su valor a entero
    posicionError = int(''.join(paridadCalculado),2)
    #Lista para corregir el mensaje
    listaMensajeCorregido = []

    #Si la posición del error es mayor a 0 (el error es existente) pero menor a 11(no excede la longitud)
    if ( posicionError > 0 and posicionError < 11):
        for i in mensaje:
            #Asignamos el mensaje a la lista para corregirlo
            listaMensajeCorregido.append(i)

        #Corregimos donde se encuentre el error aplicando un xor con 1 para invertir el bit (0^1 = 1  y 1^1 = 0)
        listaMensajeCorregido[posicionError-1] = str ( int(listaMensajeCorregido[posicionError-1]) ^ 1 )
        #Ponemos la bandera en falso
        flag = False

    mensajeCorregido = obtenerParidadMensaje(''.join(listaMensajeCorregido))[1]
    #Regresamos el mensaje recibido, la bandera y el mensaje ya corregido (en caso de no haber corrección regresa nulo)
    return mensajeRecibido, flag, mensajeCorregido


#--------------------------------------------------------------------------
#METODO PARA PROBAR LA CLASE
def prueba():
    #Simulamos el proceso de envío de un mensaje
    #mensaje original
    mensaje = '0110101'
    print(f"Mensaje original: {mensaje}")
    #mensaje a enviar
    mensajeEnviado = obtenerMensajeEnviar(mensaje)
    print(f"Mensaje enviado: {mensajeEnviado}")
    print("--------------------")
    #Una vez que se recibe se comprueba y se corrige (en caso de ser necesario)
    mensajeRecibido = comprobarMensajeOg(mensajeEnviado)
    print(f"Mensaje Recibido: {mensajeRecibido[0]}, ¿Llegó correcto? {mensajeRecibido[1]}, Corrección {mensajeRecibido[2]}")

if __name__ == '__main__':
    prueba()