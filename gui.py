#  GUI DEL EMISOR QUE NOS PERMITE IMPLEMENTAR 
#   LAS FUNCIONES DE LAS CLASES CRC Y HAMMING UTILIZANDO UNA CONEXION ENTRE DISPOSITIVOS

#---------------------------------------------------------------
# INVOCACION DE LIBRERIAS Y CLASES 
import tkinter as tk
from utils import tamañoWidget
from utils import binario
from utils import crc
from utils import conexion
#  canva principal
canva = tk.Tk()
canva.title("MARCOS JUAREZ - GAEL COSTILLA")

#---------------------------------------------------------------
def actualizar_binario( event ):
        #mensaje obtendra lo que sta dentro de nuesto text area, desde la posicion 1 hasta el final 
        # y borramos los espaciosW
    '''mensaje = area_texto.get( "1.0", tk.END ).strip()
    binario = ' '.join (format( ord( caracter ), '07b' ) for caracter in mensaje )
    area_Binario.delete( 1.0, tk.END )
    area_Binario.insert( tk.END, binario )'''
    mensaje = area_texto.get( "1.0", tk.END ).strip()
    m_binario = binario.toBin(mensaje)
    area_Binario.delete( 1.0, tk.END )
    area_Binario.insert( tk.END, m_binario )
#---------------------------------------------------------------------
# Variable para almacenar el Text adicional
nuevo_text_area = None
#-----------------------------------------------------------
# Función que se llama al seleccionar un elemento en la lista
def seleccionado(event):
    global nuevo_text_area
    global valor_seleccionado
    seleccion1 = lista.get( lista.curselection() )
    setSelected( seleccion1 )
    # Si se selecciona el elemento 3 o 4, crea y muestra un nuevo Text
    if seleccion1 in ["3", "4"]:
        if nuevo_text_area:
            nuevo_text_area.destroy()
            label_nuevo_area.destroy() 
        crear_nuevo_text_area()
    else:
        if nuevo_text_area:
            nuevo_text_area.destroy()
            label_nuevo_area.destroy()
    return seleccion1
#-----------------------------------------------------------
#funcion de selecion de lista      
def setSelected( seleccion ):
    global selected
    selected = seleccion
#-----------------------------------------------------------    
# Función para crear y mostrar un nuevo Text
def crear_nuevo_text_area():
    global nuevo_text_area, label_nuevo_area
    label_nuevo_area = tk.Label(canva, text="Ingresa mensaje:")
    label_nuevo_area.pack( pady = 5 )
    nuevo_text_area = tk.Text( canva, height = 5, width = 40 )
    nuevo_text_area.pack( pady = 10 )

#-----------------------------------------------------------
# Establecer el color de fondo de la ventana
canva.configure( background = "#0a0a0a" )  
#-----------------------------------------------------------
#darle tamaño a nuestro area de ventana
canva.geometry( "700x800" )

#-----------------------------------------------------------
# Crear un widget de etiqueta de titulo
label = tk.Label( canva, text = "CRC/HAMMING", font = ("Helvetica", 29, "bold"), background = "#0a0a0a", foreground = "#FFFFFF" )
label.pack( pady = 10 )
#el pack pady se refiere al al padding que se le dara al widget ya sea arriba o abajo seria a su alrededor

#--------------------------------------------------------------------
#label y variable donde se teclea la ip del receptor y se almacena
label_ip= tk.Label(canva, text = "ip")
label_ip.place( x = 50, y = 50 )

ip=tk.Text( canva, height = 1, width = 15 )
ip.place( x = 80, y = 50 )

#------------------------------------------------------------------------
# label mensaje de seleccion
label = tk.Label( canva, text = " Selecciona un elemento: ", bg = "#0a0a0a", fg = "#FFFFFF" , font = ( "Helvetica",12 ) )
label.place( x = 120, y = 100 )

#------------------------------------------------------------------------
#lista de bits de mensaje
elementos = [ "3", "4", "8", "12", "16", "32", "64" ]
lista = tk.Listbox( canva, selectmode = tk.SINGLE )
lista.place( x = 320,y = 100 )

for i in elementos:
    lista.insert( tk.END, i )

lista.bind("<<ListboxSelect>>", seleccionado)



#----------------------------------------------
#area de mensaje a ingresar
label_mensaje= tk.Label( canva, text = "ingresa tu mensaje", bg = "#0a0a0a", fg = "#FFFFFF", font = ( "Helvetica", 12 ) )
label_mensaje.place(x=120,y=270)

def on_validate(P):
    return len(P) <= 50

validate_cmd = (canva.register(on_validate), '%P')


#area_texto = tk.Text(canva, height=10, width=40)

#area_texto=tamañoWidget.tam(canva, max_len=16)
#area_texto.place(x=260,y=290)
#area_texto.bind("<KeyRelease>", actualizar_binario)
#-----------------------------------------------------------
#AREA DE MENSAJE A ENVIAR
validate_cmd = ( canva.register( on_validate ), '%P' )
area_texto = tk.Text( canva, height = 10, width = 40 )
area_texto.place( x = 260,y = 290 )
area_texto.bind( "<KeyRelease>", actualizar_binario )


#----------------------------------------------------------------
#LABEL de conversion de binario
label_Binario= tk.Label( canva, text = "conversion binaria:", bg = "#0a0a0a", fg = "#FFFFFF", font = ("Helvetica", 12) )
label_Binario.place( x = 120,y = 490 )

#------------------------------
#AREA DE CONVERSION BINARIO
area_Binario = tk.Text(canva, height=10, width=40)
area_Binario.place( x = 260,y = 500 )


#--------------------------------------------
# Informacion del checkbox, declaracion
def on_checkbox_click():
    selected_value.set( "Seleccionado" if checkbox_var.get() else "No seleccionado" )

# Variable DE ESTADO
checkbox_var = tk.BooleanVar()

# Crear el Checkbutton
checkbox = tk.Checkbutton( canva, text = "seleciona si desea usar el hamming", variable = checkbox_var, command = on_checkbox_click )
checkbox.place( x = 450,y = 100 )

# Variabletest
selected_value = tk.StringVar()
selected_value.set( "No seleccionado" )

#---------------------------------------------
# Agregar un botón

def clickEnviar():
    direccionip = ip.get ( "1.0", 'end-1c' )
    if ( selected in ['3','4']):
        mensaje_binario = '0b' + nuevo_text_area.get('1.0', 'end-1c')
    else:
        mensaje_binario = '0b' + area_Binario.get ('1.0', 'end-1c')
    conexion.startClient(crc.getEnvio(mensaje_binario, selected), direccionip)
boton = tk.Button(canva, text="Enviar", command=clickEnviar)
boton.place(x=250,y=700)

canva.mainloop()