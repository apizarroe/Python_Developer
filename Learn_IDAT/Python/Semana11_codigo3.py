from tkinter import *

#Configuracion de Ventana
ventana = Tk()
ventana.title("Programación Aplicada 2")
ventana.geometry("300x300")
ventana.configure(bg="beige")

#Configuracion de etiqueta
lbl1 = Label(ventana, text="Voltaje:", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=0)

lbl2 = Label(ventana, text="Corriente:", font=("Arial",13),bg= "beige",fg="blue")
lbl2.grid(column=0, row=1)

lbl3 = Label(ventana, text="Potencia", font=("Arial",13),bg= "beige",fg="blue")
lbl3.grid(column=0, row=2)

lbl4 = Label(ventana, text="Resistencia", font=("Arial",13),bg= "beige",fg="blue")
lbl4.grid(column=0, row=3)

#Crea entradas para datos
A = Entry(ventana, font=("Arial",13), fg="black", width=10)
A.grid(column= 1, row=0, sticky="w")

B = Entry(ventana, font=("Arial",13), fg="black", width=10)
B.grid(column= 1, row=1, sticky="w")

C = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
C.grid(column=1, row=2)

D = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
D.grid(column=1, row=3)


#Crea funcion para sumatorio
def calculopotencia():
  C1 = str(eval(A.get()) * eval(B.get()))
  C.configure(text=C1)

def calculoresistencia():
  D1 = str(eval(A.get()) / eval(B.get()))
  D.configure(text=D1)

def onclick():
  calculopotencia()
  calculoresistencia()

def limpieza():
  A.delete(0, END)
  B.delete(0, END)
  C.configure(text="")
  D.configure(text="")

#Boton con comando de accion
btn = Button(ventana,text="Calcular",font=("Arial",13),bg="gray",fg="black",command=onclick)
btn.grid(column=1, row=4)

btn = Button(ventana,text="Limpiar",font=("Arial",13),bg="gray",fg="black",command=limpieza)
btn.grid(column=1, row=5)

ventana.mainloop()