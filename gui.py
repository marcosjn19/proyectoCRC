import tkinter as tk
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

# Función que se llama al seleccionar un elemento en la lista
def seleccionado(event):
    global nuevo_text_area
    seleccion1 = lista.get(lista.curselection())
    setSelected(seleccion1)
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
            
def setSelected(seleccion):
    global selected
    selected = seleccion
# Función para crear y mostrar un nuevo Text
def crear_nuevo_text_area():
    global nuevo_text_area, label_nuevo_area
    label_nuevo_area = tk.Label(canva, text="Ingresa mensaje:")
    label_nuevo_area.pack(pady=5)
    nuevo_text_area = tk.Text(canva, height=5, width=40)
    nuevo_text_area.pack(pady=10)

#-----------------------------------------------------------
# Establecer el color de fondo de la ventana
canva.configure( background = "#0a0a0a" )  # Puedes cambiar el código de color a tu preferencia

#darle tamañito al canvansito poke ta chiquito
canva.geometry( "700x800" )

# Crear un widget de etiqueta
label = tk.Label( canva, text="CRC", font=("Helvetica", 29, "bold"), background="#0a0a0a", foreground="#FFFFFF" )
label.pack( pady = 10 )
#el pack pady se refiere al al padding que se le dara al widget ya sea arriba o abajo seria a su alrededor

label_ip= tk.Label(canva, text="ip")
label_ip.place(x=50, y=50)

ip=tk.Text(canva, height=1, width=15)
ip.place(x=80, y=50)

# Crear un widget de etiqueta
label = tk.Label( canva, text = " Selecciona un elemento: ", bg="#0a0a0a", fg="#FFFFFF" , font=("Helvetica",12))
label.pack( side = tk.LEFT, padx=5, pady=4 )

elementos = [ "3", "4", "8", "12", "16", "32", "64", "84" ]
lista = tk.Listbox( canva, selectmode = tk.SINGLE )

for i in elementos:
    lista.insert(tk.END, i)
lista.pack(side=tk.LEFT, padx=5, pady=10)
lista.bind("<<ListboxSelect>>", seleccionado)

label_resultado = tk.Label(canva, text="")
label_resultado.pack(pady=10)

label_mensaje= tk.Label(canva, text="ingresa tu mensaje", bg="#0a0a0a", fg="#FFFFFF", font=("Helvetica", 12))
label_mensaje.pack(pady=10)

def on_validate(P):
    return len(P) <= 50

validate_cmd = (canva.register(on_validate), '%P')
area_texto = tk.Text(canva, height=10, width=40)
area_texto.pack(pady=10)
area_texto.bind("<KeyRelease>", actualizar_binario)


label_Binario= tk.Label(canva, text="conversion binaria:", bg="#0a0a0a", fg="#FFFFFF", font=("Helvetica", 12))
label_Binario.pack(pady=10)

area_Binario = tk.Text(canva, height=10, width=40)
area_Binario.pack(pady=10)

#---------------------------------------------
# Agregar un botón

def clickEnviar():
    direccionip = ip.get ( "1.0", 'end-1c' )
    print(direccionip)
    mensaje_binario = '0b' + area_Binario.get ('1.0', 'end-1c')
    conexion.startClient(crc.getEnvio(mensaje_binario, selected), direccionip)
boton = tk.Button(canva, text="Enviar", command=clickEnviar)
boton.pack(pady=10)

canva.mainloop()