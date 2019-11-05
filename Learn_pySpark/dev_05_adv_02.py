import pyspark
sc = pyspark.SparkContext(appName="myAppName")

import os
#os.system('dir')

# Formatos de fichero soportados
# Spark puede acceder a diferentes tipos de ficheros:
# Texto plano, CSV, ficheros sequence, JSON, protocol buffers y object files
# Soporta ficheros comprimidos
# Veremos el acceso a algunos tipos en esta clase, y dejaremos otros para más adelante

# Funciones de lectura y escritura con ficheros de texto
# sc.textFile(nombrefichero/directorio) Crea un RDD a partir las líneas de uno o varios ficheros de texto
# Si se especifica un directorio, se leen todos los ficheros del mismo, creando una partición por fichero
# Los ficheros pueden estar comprimidos, en diferentes formatos (gz, bz2,…)
# Pueden especificarse comodines en los nombres de los ficheros
# sc.wholeTextFiles(nombrefichero/directorio) Lee ficheros y devuelve un RDD clave/valor
# clave: path completo al fichero
# valor: el texto completo del fichero
# rdd.saveAsTextFile(directorio_salida) Almacena el RDD en formato texto en el directorio indicado
# Crea un fichero por partición del rdd

# Lee todos los ficheros del directorio
# y crea un RDD con las líneas
lineas = sc.textFile("./datos")
# Se crea una partición por fichero de entrada
print("Número de particiones del RDD lineas = {0}".format(
       lineas.getNumPartitions()))

# Obtén las palabras usando el método split (split usa un espacio como delimitador por defecto)
palabras = lineas.flatMap(lambda x: x.split())
print("Número de particiones del RDD palabras = {0}".format(
       palabras.getNumPartitions()))

# Reparticiono el RDD en 4 particiones       
palabras2 = palabras.coalesce(4)
print("Número de particiones del RDD palabras2 = {0}".format(
       palabras2.getNumPartitions()))

# Toma una muestra aleatoria de palabras
print(palabras2.takeSample(False, 10))

# Salva el RDD palabras en varios ficheros de salida
# (un fichero por partición)
palabras2.saveAsTextFile("./salida/salidatxt")

# Ficheros de salida
os.system('dir salida\\salidatxt\\')
#os.system('type salida\\salidatxt\\part-00002 | more')

# Lee los ficheros y devuelve un RDD clave/valor
# clave->nombre fichero, valor->fichero completo
prdd = sc.wholeTextFiles("./datos/p*.gz")
print("Número de particiones del RDD prdd = {0}\n".format(
       prdd.getNumPartitions()))

# Obtiene un lista clave/valor
# clave->nombre fichero, valor->numero de palabras
lista = prdd.mapValues(lambda x: len(x.split())).collect()
for libro in lista:
    print("El fichero {0} tiene {1} palabras".format(
           libro[0].split("/")[-1], libro[1]))

# Ficheros Sequence
# Ficheros clave/valor usados en Hadoop
# Sus elementos implementan la interfaz Writable
rdd = sc.parallelize([("a",2), ("b",5), ("a",8)], 2)
# Salvamos el RDD clave valor como fichero de secuencias
rdd.saveAsSequenceFile("./salida/sequenceoutdir2")

#Lectura del fichero
os.system("echo 'Directorio de salida'")
os.system('dir salida\\sequenceoutdir2')
os.system("echo 'Intenta leer uno de los fichero'")
os.system('type salida\\sequenceoutdir2\\part-00000')
#echo  'Lee el fichero usando Hadoop'
#/opt/hadoop/bin/hdfs dfs -text /tmp/sequenceoutdir2/part-00001

# Lo leemos en otro RDD
rdd2 = sc.sequenceFile("./salida/sequenceoutdir2", 
                       "org.apache.hadoop.io.Text", 
                       "org.apache.hadoop.io.IntWritable")
print("Contenido del RDD (rdd2) {0}".format(rdd2.collect()))

# Formatos de entrada/salida de Hadoop
# Spark puede interactuar con cualquier formato de fichero soportado por Hadoop
# - Soporta las APIs “vieja” y “nueva”
# - Permite acceder a otros tipos de almacenamiento (no fichero), p.e. HBase o MongoDB, 
# a través de saveAsHadoopDataSet y/o saveAsNewAPIHadoopDataSet

# Salvamos el RDD clave/valor como fichero de texto Hadoop (TextOutputFormat)
rdd.saveAsNewAPIHadoopFile("./salida/hadoopfileoutdir", 
                            "org.apache.hadoop.mapreduce.lib.output.TextOutputFormat",
                            "org.apache.hadoop.io.Text",
                            "org.apache.hadoop.io.IntWritable")

#Se comprueba la creacion de los archivos
os.system("echo 'Directorio de salida'")
os.system("dir salida\\hadoopfileoutdir")
os.system("type salida\\hadoopfileoutdir\\part-r-00001")

# Lo leemos como fichero clave-valor Hadoop (KeyValueTextInputFormat)
rdd3 = sc.newAPIHadoopFile("./salida/hadoopfileoutdir", 
                          "org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat",
                          "org.apache.hadoop.io.Text",
                          "org.apache.hadoop.io.IntWritable")
print("Contenido del RDD (rdd3) {0}".format(rdd3.collect()))

sc.stop()