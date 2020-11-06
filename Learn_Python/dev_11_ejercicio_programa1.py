import dev_11_ejercicio_moduloficheros

nombre_fichero =  "dev_11_ejercicio_fichero.txt"
fichero =  dev_11_ejercicio_moduloficheros.Fichero(nombre_fichero)

texto = "Esta es la primera fila del fichero.\nEsta es la segunda fila."
fichero.grabar_fichero(texto)

texto = "\nEste es un texto en la tercera fila"
fichero.incluir_fichero(texto)

print(fichero.leer_fichero())