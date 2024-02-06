from tkinter import *

#Configuracion de Ventana
ventana = Tk()
ventana.title("Programación Aplicada 2")
ventana.geometry("300x300")
ventana.configure(bg="beige")

#Configuracion de etiqueta
lbl1 = Label(ventana, text="A", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=0)

lbl2 = Label(ventana, text="B", font=("Arial",13),bg= "beige",fg="blue")
lbl2.grid(column=0, row=1)

#Crea entradas para datos
A = Entry(ventana, font=("Arial",13), fg="black", width=10)
A.grid(column= 1, row=0, sticky="w")

B = Entry(ventana, font=("Arial",13), fg="black", width=10)
B.grid(column= 1, row=1, sticky="w")

C = Label(ventana, text=" ", font=("Arial",13),bg= "beige",fg="blue")
C.grid(column=1, row=2)

#Crea funcion para sumatorio
def calculo():
  C1 = str(eval(A.get()) + eval(B.get()))
  C.configure(text=C1)

#Boton con comando de accion
btn = Button(ventana,text="Suma",font=("Arial",13),bg="gray",fg="black",command=calculo)
btn.grid(column=1, row=3)

ventana.mainloop()