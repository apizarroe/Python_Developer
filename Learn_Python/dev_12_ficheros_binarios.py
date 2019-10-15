###################Ficheros Binarios
#pickle - Modulo para ficheros binarios
import pickle
lista_colores = ["azul","verde","rojo","amarillo"]
#abrimos el fichero en modo escritura - binario
fichero = open("dev_12_fichero_colores.pckl","wb")
#Escribe la lista en el fichero
pickle.dump(lista_colores,fichero)
fichero.close()

#pickle - Modulo para leer datos de un fichero binario
import pickle
#abrimos el fichero en modo lectura - binario
fichero = open("dev_12_fichero_colores.pckl","rb")
#Lee la lista del fichero
lista_leida_fichero = pickle.load(fichero)
print(lista_leida_fichero)
fichero.close()

