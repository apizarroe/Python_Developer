###################Ficheros Texto
#Inicializamos el fichero de prueba (Abajo se explica esta función)
fichero = open("dev_11_fichero_para_leer.txt","wt")
texto_del_fichero = "Esto es un fichero de ejemplo,\nque tiene 2 líneas de texto"
texto_del_fichero = texto_del_fichero.encode("utf-8").decode("windows-1252")
fichero.write(texto_del_fichero)
fichero.close()

#Leer el fichero de texto
#abrimos el fichero en modo lectura - texto
fichero = open("dev_11_fichero_para_leer.txt","rt")
#Esto es para leer un fichero de texto, controlando los caracteres extaños.
datos_fichero = fichero.read().encode("windows-1252").decode("utf-8")
print(datos_fichero)
fichero.close()

#Grabar un fichero de texto
#abrimos el fichero en modo escritura - texto
fichero = open("dev_11_fichero_para_grabar.txt","wt")
texto_del_fichero = "Hola, esta es la línea que vamos a grabar en el fichero de texto \nEsto es un salto de línea"
texto_del_fichero = texto_del_fichero.encode("utf-8").decode("windows-1252")
#Esto es para escribir en un fichero de texto.
fichero.write(texto_del_fichero)
fichero.close()

#Incluir datos ficheros
fichero = open("dev_11_fichero_para_leer.txt","at")
cadena_para_incluir = "\nEsta es la tercera fila del fichero. Revisión"
cadena_para_incluir = cadena_para_incluir.encode("utf-8").decode("windows-1252")
fichero.write(cadena_para_incluir)
fichero.close()

#Borra Fichero
import os
os.remove("dev_11_fichero_para_leer.txt")
