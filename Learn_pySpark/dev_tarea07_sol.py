# Desarrollar un script PySpark, que, a partir de los ficheros secuencia en apat63_99-seq 
# cree un RDD clave valor, en el cual la clave es un país y el valor una lista de tuplas, 
# en la que cada tupla esté formada por un año y el número de patentes de ese país en ese año. 
# Además, debeis utilizar el contenido del fichero country_codes.txt (localizado en ../datos/country_codes.txt) 
# como una variable de broadcast y substituir el código del país por su nombre. Por último, 
# el RDD creado debe estar ordenado por el nombre del país y, para cada país, la lista de valores ordenados por año.
# Recordad que cada registro de apat63_99-seq tiene un par clave valor (país patente,año), 
# siendo tanto la clave como el valor de tipo org.apache.hadoop.io.Text.
# Preguntas de esta tarea
# ¿En cuantos años ha habido patentes asociadas a Honduras?

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from operator import add

with open("country_codes.txt") as f:
    cc = dict([line.strip().split("\t") for line in f])
ccbcast = sc.broadcast(cc)

info = sc.sequenceFile("./salida/apat63_99-seq","org.apache.hadoop.io.Text","org.apache.hadoop.io.Text").\
    map(lambda x: (x[0]+","+x[1].split(",")[1], 1)).reduceByKey(add).map(lambda x: (x[0].split(",")[0],[(x[0].split(",")[1],x[1])])).\
        reduceByKey(add).map(lambda x: (ccbcast.value[x[0]],sorted(x[1]))).sortByKey()

print(len(info.lookup("Honduras")[0]))

sc.stop()