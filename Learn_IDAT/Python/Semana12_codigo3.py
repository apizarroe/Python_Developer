import serial
from tkinter import *
from datetime import datetime

ventana = Tk()
ventana.title("Lectura de LM35")
ventana.geometry("500x1000")
ventana.configure(bg="beige")

lbl1 = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=0)

lbl1 = Label(ventana, text="    ", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=1)

lbl1 = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
lbl1.grid(column=0, row=2)

A = Label(ventana, text="", font=("Arial",13),bg= "beige",fg="blue")
A.grid(column= 1, row=1)

def registrardatos():
    i = 0
    puerto = serial.Serial('COM3',9600)
    valores_array = []
    
    f = open("LM35.txt","w")
    while(i < 20):
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        valor = puerto.readline().decode('utf-8').rstrip()
        log = str(current_time) + "\t" + str(valor) + "\n"
        valores_array.append(log)
        f.write(log)
        i = i+1
    f.close()
    puerto.close()
    
    array_text = "\n".join(valores_array)
    A.config(text=array_text)

def onclick():
  registrardatos()

btn = Button(ventana,text="Iniciar",font=("Arial",13),bg="gray",fg="black",command=onclick)
btn.grid(column=1, row=3)

ventana.mainloop()