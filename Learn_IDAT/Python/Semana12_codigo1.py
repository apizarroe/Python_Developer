from tkinter import *

ventana = Tk()
ventana.title("Aplicación de Ventas")
ventana.geometry("300x300")
ventana.configure(bg="beige")

lbl1 = Label(ventana, text="Unidades Adquiridas:", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=0)

lbl2 = Label(ventana, text="Importe Comprado:", font=("Arial",13),bg= "beige",fg="blue")
lbl2.grid(column=0, row=1)

lbl3 = Label(ventana, text="Importe Descuento:", font=("Arial",13),bg= "beige",fg="blue")
lbl3.grid(column=0, row=2)

lbl4 = Label(ventana, text="Total a Pagar:", font=("Arial",13),bg= "beige",fg="blue")
lbl4.grid(column=0, row=3)

A = Entry(ventana, font=("Arial",13), fg="black", width=10)
A.grid(column= 1, row=0, sticky="w")

B = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
B.grid(column= 1, row=1)

C = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
C.grid(column=1, row=2)

D = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
D.grid(column=1, row=3)

def calculosubtotal(cantidad):
    if(cantidad > 0):
        if (cantidad>=1 and cantidad<=25):
            prc_unit = 27.7
            subtotal = cantidad * prc_unit
        if (cantidad>=26 and cantidad<=50):
            prc_unit = 25.5
            subtotal = cantidad * prc_unit
        if (cantidad>=51 and cantidad<=75):
            prc_unit = 23.5
            subtotal = cantidad * prc_unit
        if (cantidad>=76):
            prc_unit = 21.5
            subtotal = cantidad * prc_unit
    return round(subtotal,3)
        
def calculodescuento(cantidad, subtotal):
    if(cantidad > 50):
        descuento = subtotal * (0.15)
    if(cantidad <= 50):
        descuento = subtotal * (0.05)
    return round(descuento,3)

def calculototal(subtotal, descuento):
    total = subtotal - descuento
    return round(total,3)

def calculocompra():
  cantidad = eval(A.get())
  subtotal = calculosubtotal(cantidad)
  descuento = calculodescuento(cantidad, subtotal)
  total = calculototal(subtotal, descuento)
  B1 = str(subtotal)
  B.configure(text=B1)
  C1 = str(descuento)
  C.configure(text=C1)
  D1 = str(total)
  D.configure(text=D1)

def escribefichero():
    f = open("historial_ventas.txt","a")
    f.write("Cantidad Comprada: " + A.get() + "\n")
    f.write("Importe de compra: " + B.cget("text") + "\n")
    f.write("Importe de descuento: " + C.cget("text") + "\n")
    f.write("Importe a pagar: " + D.cget("text") + "\n")
    f.write("\n")
    f.close()

def onclick():
  calculocompra()
  escribefichero()

def limpieza():
  A.delete(0, END)
  B.configure(text="")
  C.configure(text="")
  D.configure(text="")

btn = Button(ventana,text="Calcular",font=("Arial",13),bg="gray",fg="black",command=onclick)
btn.grid(column=1, row=4)

btn = Button(ventana,text="Limpiar",font=("Arial",13),bg="gray",fg="black",command=limpieza)
btn.grid(column=1, row=5)

ventana.mainloop()