import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

###################Etiqueta
texto = "Hola mundo"
#Se crea la etiqueta y se le asigna el texto
etiqueta = tkinter.Label(raiz,text=texto)
#Se personaliza la fuente del texto
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack()

###################Entry
#Creamos nuestro componente entry (entrada de datos)
entrada = tkinter.Entry(raiz)
entrada.config(justify="center")
#entrada.config(justify="center",show="*"). Si fuera un password
entrada.pack()

###################Text
#Creamos nuestro componente Text (texto de varias líneas)
entrada = tkinter.Text(raiz)
#Personalizamos el campo Texto
entrada.config(width=20, height=10, font=("Verdana",15), padx=10, pady=10, fg="green", selectbackground="lightgrey")
entrada.pack()

raiz.mainloop()