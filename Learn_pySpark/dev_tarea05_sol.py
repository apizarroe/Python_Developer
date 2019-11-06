# A partir del fichero apat63_99.txt, crear un conjunto de ficheros secuencia, que se almacenarán en el directorio 
# apat63_99-seq. En estos ficheros, la clave tiene que ser el país (campo “COUNTRY”) y el valor un string formado 
# por el número de patente (campo “PATENT”) y el año de concesión (campo “GYEAR”) separados por una coma. 
# Una línea de esto ficheros será, por ejemplo:
# BE     3070801,1963
# Preguntas de esta tarea
# Después de obtener los ficheros secuencia, leelos en otro RDD y a partir de este obtén el número de patentes 
# asociados a EE.UU. Indica el número.
import pyspark
sc = pyspark.SparkContext(appName="myAppName")
import os
os.system('rmdir /S /Q salida\\apat63_99-seq')
# Se realiza la lectura del archivo apat63_99.txt
rdd = sc.textFile("./datos/apat63_99.txt")
# Se realiza el filtrado de la primera linea (cabecera)
# Se splitea cada linea del archivo
# Se crea un prrd ('COUNTRY', 'PATENTE,AÑO')
prdd = rdd.filter(lambda l: not l.startswith('"PATENT"')).map(lambda l: l.split(",")).\
    map(lambda lista: (lista[4].strip('"'), lista[0]+","+lista[1]))
print(prdd.take(2))
# El contenido de prrd se escribe en un SequenceFile
prdd.saveAsSequenceFile("./salida/apat63_99-seq")
# El SequenceFile creado se lee en prrd
prdd2 = sc.sequenceFile("./salida/apat63_99-seq")
# Se realiza el conteo de los registros que tienen como llave 'US'
print(prdd2.countByKey()['US'])

sc.stop()