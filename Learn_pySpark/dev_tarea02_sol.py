# Ver el archivo de recursos adjunto que contiene indicaciones sobre los ficheros que utilizaremos como entrada en esta 
# y las subsiguientes tareas.
# TAREA: Obtener las citas recibidas por cada patente
# Escribir un programa PySpark que, a partir del fichero cite75_99.txt, obtenga el número de citas que recibe cada patente.
# Preguntas de esta tarea
# ¿Cuántas citas ha recibido la patente número 3986997?
# ¿Cuántas citas ha recibido la patente número 4418284?
# ¿Cuántas citas ha recibido la patente número 4314227?
# ¿Cuántas citas ha recibido la patente número 3911418?
# ¿Cuál es la patente que ha recibido más citas? Indica el número de patente.

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

###############SOLUCION DE PROFESOR
from operator import add
# Se realiza la lectura del archivo cite75_99.txt
# Se realiza el filtrado de la primera linea (cabecera)
# Se toma el forma un prdd con el citado y el valor 1
# Se realiza un reduceByKey con 'add' a los valores, finalmente se cachea el prdd
rdd = sc.textFile("./datos/cite75_99.txt").filter(lambda l: '"CITING","CITED"' not in l).\
    map(lambda l: (l.split(",")[1],1)).reduceByKey(add).cache()
rdd2 = rdd.sortByKey()
# Se realiza la busqueda de las llaves, para conocer la cantidad de citas
print(rdd2.lookup('3986997'))
print(rdd2.lookup('4418284'))
print(rdd2.lookup('4314227'))
print(rdd2.lookup('3911418'))
# Se invierte el orden de los prdd (# de citas, citados), 
# entonces se ordena por llave para encontrar los que tiene mayor numero de citas
rdd1 = rdd.map(lambda x: (x[1],x[0])).sortByKey(False)
print(rdd1.take(1))
#Otra opcion es invertir el orden de los campos y usar el countByKey()

sc.stop()