import pyspark
sc = pyspark.SparkContext(appName="myAppName")

# PERSISTENCIA
# En Scala y Java, el nivel por defecto es MEMORY_ONLY
# En Python, los datos siempre se serializan (por defecto como objetos pickled)
# Los niveles MEMORY_ONLY, MEMORY_AND_DISK son equivalentes a MEMORY_ONLY_SER, MEMORY_AND_DISK_SER
# Es posible especificar serialización marshal al crear el SparkContext
# sc = SparkContext(master="local", appName="Mi app", serializer=pyspark.MarshalSerializer())
# Recuperación de fallos
# Si falla un nodo con datos almacenados, el RDD se recomputa
# Añadiendo _2 al nivel de persistencia, se guardan 2 copias del RDD

rdd = sc.parallelize(range(1000),10)
#Con esta función se verifica si el RDD se esta persistiendo.
print(rdd.is_cached)
#Con esta función se asigna persistencia y el tipo de la misma.
rdd.persist(pyspark.StorageLevel.MEMORY_AND_DISK_SER_2)
print(rdd.is_cached)
#Con rdd.getStorageLevel() se obtiene la persistencia del RDD.
print("Nivel de persistencia de rdd: {0}".format(rdd.getStorageLevel()))
#La persistencia no es herdada!!!!
rdd2 = rdd.map(lambda x: x*x)
print(rdd2.is_cached)
#Se cachea el RRD
rdd2.cache()
print(rdd2.is_cached)
print("Nivel de persistencia de rdd2: {0}".format(rdd2.getStorageLevel()))
#Se quita la persistencia a un RDD
rdd2.unpersist()
print(rdd2.is_cached)


# PARTICIONADO
# El número de particiones es función del tamaño del cluster o el número de bloques del fichero en HDFS
# Es posible ajustarlo al crear u operar sobre un RDD
# El paralelismo de RDDs que derivan de otros depende del de sus RDDs padre
# Dos funciones útiles:
# rdd.getNumPartitions() devuelve el número de particiones del RDD
# rdd.glom() devuelve un nuevo RDD juntando los elementos de cada partición en una lista

rdd = sc.parallelize([1,2,3,4,2,4,1],4)
pairs = rdd.map(lambda x: (x , x))
print("RDD pairs = {0}".format(
        pairs.collect()))
print("Particionado de pairs: {0}".format(
        pairs.glom().collect()))
print("Número de particiones de pairs = {0}".format(
        pairs.getNumPartitions()))

# Reducción manteniendo el número de particiones
print("Reducción con 4 particiones: {0}".format(
        pairs.reduceByKey(lambda x, y: x+y).glom().collect()))

# Reducción modificando el número de particiones
print("Reducción con 2 particiones: {0}".format(
        pairs.reduceByKey(lambda x, y: x*y, 2).glom().collect()))

# repartition(n) devuelve un nuevo RDD que tiene exactamente n particiones
# coalesce(n) más eficiente que repartition, minimiza el movimiento de datos
# Solo permite reducir el número de particiones
# partitionBy(n,[partitionFunc]) Particiona por clave, usando una función de particionado (por defecto, un hash de la clave)
# Solo para RDDs clave/valor
# Asegura que los pares con la misma clave vayan a la misma partición
pairs5 = pairs.repartition(5)
print("pairs5 con {0} particiones: {1}".format(
        pairs5.getNumPartitions(),
        pairs5.glom().collect()))

pairs2 = pairs5.coalesce(2)
print("pairs2 con {0} particiones: {1}".format(
        pairs2.getNumPartitions(),
        pairs2.glom().collect()))

pairs_clave = pairs2.partitionBy(4)
print("Particionado por clave ({0} particiones): {1}".format(
        pairs_clave.getNumPartitions(),
        pairs_clave.glom().collect())) 

sc.stop()