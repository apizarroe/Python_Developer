import pyspark
sc = pyspark.SparkContext(appName="myAppName")

#Ejemplo en PySpark de generar un RDD
rdd1 = sc.parallelize([1,2,3])
import numpy as np
#Ejemplo en PySpark de generar un RDD con valores de 0 a 99
rdd2=sc.parallelize(np.array(range(100)))
#Impresion de la lista de valores
print(rdd2.collect())
#Impresion de la lista de valores segmentados por particion
print(rdd2.glom().collect())

#Ejemplo en PySpark de Lectura de Fichero (fichero quijote.txt)
quijote = sc.textFile("quijote.txt")
#Se toma solo la primera linea del RDD
print(quijote.take(1))
print(" ")
#Se toma las primeras 'n' lineas del RDD
print(quijote.take(100))

#Asignacion manual de particiones para el procesamiento de RDDs
rdd = sc.parallelize([1,2,3,4], 2)
print(rdd.glom().collect())
#Se muestra la cantidad de particiones generadas
print("# de Particiones en total: " + str(rdd.getNumPartitions()))

#Transformaciones con RDD
quijs = quijote.filter(lambda l: "Quijote" in l) #Busca las lineas conteniendo "Quijote"
sanchs = quijote.filter(lambda l: "Sancho" in l) #Busca las lineas conteniendo "Sancho"
quijssancs = quijs.intersection(sanchs) #Realiza la interseccion y no muestra nada
quijssancs.cache()

#Acciones con RDD
nqs = quijssancs.count() #Se realiza el conteo de las lineas
print("Líneas con Quijote y Sancho: {0}".format(nqs)) # Se imprime la cantidad de linea
print(" ")
for l in quijssancs.takeSample(False,10): #Se toma una muestra de 10 y se imprimen
    print(l)

sc.stop()