# Desarrollar un script PySpark, que, a partir de los ficheros secuencia en apat63_99-seq 
# cree un RDD clave valor, en el cual la clave es un país y el valor una lista de tuplas, 
# en la que cada tupla esté formada por un año y el número de patentes de ese país en ese año. 
# Además, debeis utilizar el contenido del fichero country_codes.txt (localizado en ./datos/country_codes.txt) 
# como una variable de broadcast y substituir el código del país por su nombre. Por último, 
# el RDD creado debe estar ordenado por el nombre del país y, para cada país, la lista de valores ordenados por año.
# Recordad que cada registro de apat63_99-seq tiene un par clave valor (país patente,año), 
# siendo tanto la clave como el valor de tipo org.apache.hadoop.io.Text.
# Preguntas de esta tarea
# ¿En cuantos años ha habido patentes asociadas a Honduras?

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from operator import add
# Se realiza la lectura del archivo country_codes.txt
# Se remueve los espacios y se splitea por tab (\t)
# Se crea una variable broadcast 'ccbcast'
with open("./datos/country_codes.txt") as f:
    cc = dict([line.strip().split("\t") for line in f])
ccbcast = sc.broadcast(cc)
# Se realiza la lectura del sequenceFile apat63_99-seq, Key y Value = org.apache.hadoop.io.Text ('COUNTRY', 'PATENTE,AÑO')
# Se crea un prdd ('COUNTRY,AÑO', 1) y se aplica reduceByKey para contar las repeticiones
# Se crea un prdd ('COUNTRY',[(AÑO,#PATENTES)]) y se aplica reduceByKey para agrupar los objetos de la misma llave
# Se utiliza el dict (var broadcast) para obtner el nombre completo de COUNTRY, finalmente se ordena por Key
info = sc.sequenceFile("./salida/apat63_99-seq","org.apache.hadoop.io.Text","org.apache.hadoop.io.Text").\
    map(lambda x: (x[0]+","+x[1].split(",")[1], 1)).reduceByKey(add).\
    map(lambda x: (x[0].split(",")[0],[(x[0].split(",")[1],x[1])])).\
    reduceByKey(add).map(lambda x: (ccbcast.value[x[0]],sorted(x[1]))).sortByKey()
print(info.take(10))
# Se busca el arreglo que tiene como llave Honduras y se calcula su longitud
print(len(info.lookup("Honduras")[0]))
sc.stop()