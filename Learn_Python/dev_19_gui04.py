import tkinter
from tkinter import messagebox
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

###################Informacion
def avisar():
    tkinter.messagebox.showinfo("Titulo", "Mensaje con la informacion")

#Crear componente "popup" (ventana de información)
button1 = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
button1.pack()

###################Pregunta
def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo", "¿Quieres borrar este fichero?")
    if (resultado == "yes"):
        print("Si, quiero borrar  el fichero")
    else:
        print("No, quiero borrar  el fichero")

#Crear componente para preguntar o confirmar algo
button2 = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
button2.pack()

###################Confirmar Fichero
def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)

button3 = tkinter.Button(raiz, text="Pulsar para empezar", command=abrirfichero)
button3.pack()

raiz.mainloop()