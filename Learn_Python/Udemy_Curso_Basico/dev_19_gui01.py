#tkinter - Componente raiz
import tkinter

#Para invocar el objeto raiz (Interfaz Grafica)
raiz = tkinter.Tk()
#Se asigna el titulo "Mi programa"
raiz.title("Mi programa")

#Creamos el componente frame
frame = tkinter.Frame(raiz)
frame.config(bg="blue",width=400,height=300)
frame.pack()

#Se mantiene en ejecución de manera continua
raiz.mainloop()
