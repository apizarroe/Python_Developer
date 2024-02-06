import serial,time
from tkinter import *

puerto = serial.Serial('COM3',9600)
time.sleep(2)

ventana = Tk()
ventana.title("Lectura de LM35")
ventana.geometry("500x1000")
ventana.configure(bg="beige")

def ENCENDIDO():
  puerto.write(b"a")
  
btn = Button(ventana,text="ENCENDIDO",font=("Arial",13),bg="gray",fg="black",command=ENCENDIDO)
btn.grid(column=2,row=3)

def APAGADO():
  puerto.write(b"b")
  
btn = Button(ventana,text="APAGADO",font=("Arial",13),bg="gray",fg="black",command=APAGADO)
btn.grid(column=2,row=4)

def FINALIZAR():
  puerto.close()
  
btn = Button(ventana,text="FINALIZAR",font=("Arial",13),bg="gray",fg="black",command=FINALIZAR)
btn.grid(column=2,row=5)

ventana.mainloop()