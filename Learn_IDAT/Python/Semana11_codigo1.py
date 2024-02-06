from tkinter import *

#Configuracion de Ventana
ventana = Tk()
ventana.title("Programación Aplicada 2")
ventana.geometry("300x300")
ventana.configure(bg="beige")

#Configuracion de etiqueta
lbl1 = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=0)

#Metodo de accion de boton
def verNombre():
  lbl1.configure(text="Aldo")

def verApellido():
  lbl1.configure(text="Pizarro Espinoza")

def verCodigo():
  lbl1.configure(text="U17202187")

#Boton con comando de accion
btn = Button(ventana,text="Nombres",font=("Arial",13),bg="gray",fg="black",command=verNombre)
btn.grid(column=0, row=1)

btn = Button(ventana,text="Apellidos",font=("Arial",13),bg="gray",fg="black",command=verApellido)
btn.grid(column=1, row=1)

btn = Button(ventana,text="Codigo IDAT",font=("Arial",13),bg="gray",fg="black",command=verCodigo)
btn.grid(column=2, row=1)

ventana.mainloop()