import tkinter as tk
from utils import conexion
from utils import crc
from utils import binario

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
    label_resultado.config( text = f"Seleccionado: {seleccionado}")
#---------------------------------------------------------------



#-----------------------------------------------------------
# Establecer el color de fondo de la ventana
canva.configure( background = "#2E8B57" )  # Puedes cambiar el código de color a tu preferencia

#darle tamañito al canvansito poke ta chiquito
canva.geometry( "700x700" )

# Crear un widget de etiqueta
label = tk.Label( canva, text="CRC receptor", font=("Helvetica", 29, "bold"),background="#2E8B57", foreground="#000000" )
label.pack( pady = 10 )
#el pack pady se refiere al al padding que se le dara al widget ya sea arriba o abajo seria a su alrededor

# Crear un widget de etiqueta
label = tk.Label( canva, text = " Selecciona un elemento:" )
label.place(x=120,y=100)

elementos = [ "3", "4", "8", "12", "16", "32", "64", "84" ]
lista = tk.Listbox( canva, selectmode = tk.SINGLE )
lista.place(x=230,y=100)

for i in elementos:
    lista.insert(tk.END, i)

lista.bind("<<ListboxSelect>>", seleccionado)

label_resultado = tk.Label(canva, text="")
lista.place(x=260,y=100)

label_mensaje= tk.Label(canva, text="Mensaje recibido", bg="#0a0a0a", fg="#FFFFFF", state=tk.DISABLED )
label_mensaje.place(x=130,y=270)


area_texto = tk.Label(canva, height=10, width=40, state=tk.DISABLED, textvariable=mensajeRecibido )
area_texto.place(x=250,y=270)


label_Binario= tk.Label(canva, text="conversion binaria:", bg="#0a0a0a", fg="#FFFFFF")
label_Binario.place(x=130,y=490)

area_Binario = tk.Label(canva, height=10, width=40, textvariable=mensajeBinarioRecibido)
area_Binario.place(x=250,y=490)

#-------------------------------------------------

label_bandera = tk.Label(canva, text= " Bandera ")
label_bandera.place(x=50, y=50)

text_bandera = tk.Label(canva,  height=2, width=4)
text_bandera.place(x=120, y=50)
ip_txt = tk.StringVar()
ip_txt.set(conexion.obtener_ip())

label_ip_recibida = tk.Label ( canva, textvariable=ip_txt )
label_ip_recibida.place(x=500, y=50)



def recibirMensaje():
    mensaje = conexion.startServer()
    datosMensaje = crc.obtenerMensajeOG(mensaje, lista.get ( lista.curselection() ) )
    mensajeBinarioRecibido.set(datosMensaje[0][2::])
    mensajeBinstr = mensajeBinarioRecibido.get()
    mensajeRecibido.set(binario.fromBin(mensajeBinstr))

boton = tk.Button(canva, text="RECIBIR", command=recibirMensaje)
boton.place(x = 550, y = 100)

canva.mainloop()