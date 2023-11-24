import tkinter as tk
#  canva principal
canva = tk.Tk()
canva.title("MARCOS JUAREZ - GAEL COSTILLA")
#---------------------------------------------------------------
def seleccionado( event ):
    seleccionado = lista.get( lista.curselection() )
    label_resultado.config( text = f"Seleccionado: {seleccionado}")
#---------------------------------------------------------------
def actualizar_binario( event ):
        #mensaje obtendra lo que sta dentro de nuesto text area, desde la posicion 1 hasta el final 
        # y borramos los espaciosW
    mensaje = area_texto.get( "1.0", tk.END ).strip()
    binario = ' '.join (format( ord( caracter ), '08b' ) for caracter in mensaje )
    area_Binario.delete( 1.0, tk.END )
    area_Binario.insert( tk.END, binario )
#---------------------------------------------------------------------


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
label = tk.Label( canva, text = " Selecciona un elemento: " )
label.pack( side = tk.LEFT, padx=5, pady=4 )

elementos = [ "3", "4", "8", "12", "16", "32", "64", "84" ]
lista = tk.Listbox( canva, selectmode = tk.SINGLE )

for i in elementos:
    lista.insert(tk.END, i)
lista.pack(side=tk.LEFT, padx=5, pady=10)
lista.bind("<<ListboxSelect>>", seleccionado)

label_resultado = tk.Label(canva, text="")
label_resultado.pack(pady=10)

label_mensaje= tk.Label(canva, text="Mensaje recibido", bg="#0a0a0a", fg="#FFFFFF", state=tk.DISABLED)
label_mensaje.pack(pady=10)


area_texto = tk.Text(canva, height=10, width=40, state=tk.DISABLED)
area_texto.pack(pady=10)
area_texto.bind("<KeyRelease>", actualizar_binario)


label_Binario= tk.Label(canva, text="conversion binaria:", bg="#0a0a0a", fg="#FFFFFF")
label_Binario.pack(pady=10)

area_Binario = tk.Text(canva, height=10, width=40, )
area_Binario.pack(pady=10)

#---------------------------------------------

label_bandera = tk.Label(canva, text= " Bandera ")
label_bandera.place(x=50, y=50)

text_bandera = tk.Label(canva,  height=2, width=4)
text_bandera.place(x=120, y=50)

label_ip_recibida = tk.Label(canva, text= " ip recibida ")
label_ip_recibida.place(x=500, y=50)


canva.mainloop()