#   GUI DEL RECEPTOR QUE NOS PERMITE RECIBIR LA INFORMACION ENVIADA POR EL EMISOR APLICANDO
#   LAS FUNCIONES DE LAS CLASES CRC Y HAMMING UTILIZANDO UNA CONEXION ENTRE DISPOSITIVOS

#---------------------------------------------------------------
# INVOCACION DE LIBRERIAS Y CLASES 
import tkinter as tk
from utils import conexion
from utils import crc
from utils import binario
from utils import hamming
#-------------------------------------------------------------------
#  canva principal
canva = tk.Tk()
global mensajeBinarioRecibido
mensajeBinarioRecibido = tk.StringVar()

global mensajeRecibido
mensajeRecibido = tk.StringVar()

canva.title("MARCOS JUAREZ - GAEL COSTILLA")
#---------------------------------------------------------------
def seleccionado( event ):
    seleccionado = lista.get( lista.curselection() )
# label_resultado.config( text = f"Seleccionado: {seleccionado}")
#---------------------------------------------------------------
# Establecer el color de fondo de la ventana
canva.configure( background = "#2E8B57" )  # Puedes cambiar el código de color a tu preferencia
#---------------------------------------------------------------
#darle tamañito al canva
canva.geometry( "700x700" )
#---------------------------------------------------------------
# Crear un widget de etiqueta
label = tk.Label( canva, text = "CRC/DISTANCIA HAMMING receptor", font=("Helvetica", 29, "bold"), background = "#2E8B57", foreground = "#000000" )
label.pack( pady = 10 )

#---------------------------------------------------------------
#el pack pady se refiere al al padding que se le dara al widget ya sea arriba o abajo seria a su alrededor
# Crear un widget de etiqueta, el .place nos da una ubicacion especifica dentro de nuestra ventana
label = tk.Label( canva, text = " Selecciona un elemento:" )
label.place( x = 70,y = 100 )

#--------------------------------------------------------
#lista desplegable con los elementos que podemos elegir en nuestra lista
elementos = [ "3", "4", "8", "12", "16", "32", "64" ]
lista = tk.Listbox( canva, selectmode = tk.SINGLE )
lista.place( x = 230,y = 100 )

#--------------------------------------
#recorrido de lista con los elementos asignados
for i in elementos:
    lista.insert(tk.END, i)

lista.bind("<<ListboxSelect>>", seleccionado)


#---------------------------------------------------------
#espacio donde mandamos el mensaje  label y area
label_mensaje= tk.Label(canva, text = "Mensaje recibido", bg  ="#0a0a0a", fg="#FFFFFF", state=tk.DISABLED )
label_mensaje.place(x=130,y=270)

#---------------------------------------------------
#el area cuenta con propiedades de solo lectura
area_texto = tk.Label(canva, height = 10, width = 40, state = tk.DISABLED, textvariable = mensajeRecibido )
area_texto.place( x = 250,y = 270 )

#-------------------------------------------------------
#el area de la conversion a binario del mensaje
label_Binario= tk.Label( canva, text="conversion binaria:", bg="#0a0a0a", fg="#FFFFFF" )
label_Binario.place( x = 130, y = 490 )

area_Binario = tk.Label( canva, height = 10, width = 40, textvariable = mensajeBinarioRecibido )
area_Binario.place( x = 250,y = 490)

#-------------------------------------------------
#apartado donde asignamos la bandera que nos verifica la llegada del mensaje
label_bandera = tk.Label( canva, text= " Bandera " )
label_bandera.place( x = 50, y = 50)

text_bandera = tk.Label( canva,  height = 2, width = 4)
text_bandera.place( x = 120, y = 50 )

#----------------------------------------------
#ip del receptor
ip_txt = tk.StringVar()
ip_txt.set(conexion.obtener_ip())

label_ip_recibida = tk.Label ( canva, textvariable=ip_txt )
label_ip_recibida.place(x=500, y=50)
#--------------------------------------------
# Informacion del checkbox, declaracion
def on_checkbox_click():
    selected_value.set( "Seleccionado" if checkbox_var.get() else "No seleccionado" )

# Variable DE ESTADO
checkbox_var = tk.BooleanVar()

# Crear el Checkbutton
checkbox = tk.Checkbutton( canva, text = "seleciona si desea usar el hamming", variable = checkbox_var, command = on_checkbox_click )
checkbox.place( x = 450,y = 200 )

# Variabletest
selected_value = tk.StringVar()
selected_value.set( "No seleccionado" )



#-------------------------------------------------
#recepcion de mensaje
def recibirMensaje():
    #verificacion de conecion
    mensaje = conexion.startServer()
    #obtencion de mensaje
    if ( checkbox_var.get() ): #Si el envio se recibe por Hamming
        datosMensaje = hamming.comprobarMensajeOg(mensaje)
        mensajeBinarioRecibido.set(datosMensaje[0])
        correcto = datosMensaje[1]
        #Si llego correctamente muestra el mensaje tal cual
        if (correcto):
            mensajeBinarioRecibido.set(datosMensaje[0])
        else: #Sino, muestra el corregido
            mensajeBinarioRecibido.set(datosMensaje[2])
        mensajeBinstr = mensajeBinarioRecibido.get()
        mensajeRecibido.set(binario.fromBin(mensajeBinstr))
        if ( correcto ):
            text_bandera.config(background="Green")
        else:
            text_bandera.config(background="Red")
    else: #Si no
        datosMensaje = crc.obtenerMensajeOG(mensaje, lista.get ( lista.curselection() ) )
        mensajeBinarioRecibido.set(datosMensaje[0][2::])
        mensajeBinstr = mensajeBinarioRecibido.get()
        mensajeRecibido.set(binario.fromBin(mensajeBinstr))
        if ( datosMensaje[2] == True ):
            text_bandera.config(background="Green")
        else:
            text_bandera.config(background="Red")

boton = tk.Button(canva, text="RECIBIR", command=recibirMensaje)
boton.place(x = 550, y = 100)

canva.mainloop()