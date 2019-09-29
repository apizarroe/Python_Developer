#Leer el fichero de texto
fichero = open("dev_11_ficherotexto.txt","rt")
#Esto es para codificar y decodificar, controlando los caracteres extaños.
datos_fichero = fichero.read().encode("windows-1252").decode("utf-8")
print(datos_fichero)

