import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

###################Button
#Definimos la funcion accion
def accion():
    print("Hola mundo")
#Creamos el componente button (boton, para ejecutar una accion cuando se pulsa)
boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()

###################RadioButton
#Definimos la funcion seleccionar
def seleccionar():
    print("La opción seleccionada es {}".format(opcion.get()))

opcion=tkinter.IntVar() 
#Creamos los radiobutton
radiobutton1 = tkinter.Radiobutton(raiz, text="Opción 1", variable=opcion, value=1, command=seleccionar)
radiobutton1.pack()
radiobutton1 = tkinter.Radiobutton(raiz, text="Opción 2", variable=opcion, value=2, command=seleccionar)
radiobutton1.pack()
radiobutton1 = tkinter.Radiobutton(raiz, text="Opción 3", variable=opcion, value=3, command=seleccionar)
radiobutton1.pack()

###################CheckButton
#Definimos la funcion verificar
def verificar():
    valor = check1.get()
    if (valor == 1):
        print("El check esta activado")
    else: 
        print("El check esta desactivado")

check1 = tkinter.IntVar()
#Creamos el checkbutton
button1 = tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
button1.pack()

raiz.mainloop()