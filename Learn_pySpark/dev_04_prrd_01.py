import pyspark
sc = pyspark.SparkContext(appName="myAppName")

##########Creación de Pair RDDs
#A partir de una lista de tuplas
prdd = sc.parallelize([('a',2),('b',5),('a',3)])
print(prdd.collect())
prdd = sc.parallelize(zip(['a','b','c'],range(3)))
print(prdd.collect())

# Ejemplo usando un fichero
# Para cada línea ontenemos una tupla, siendo el primer elemento
# la primera palabra de la línes, y el segundo la línea completa
linesrdd = sc.textFile("quijote.txt")
prdd = linesrdd.map(lambda x: (x.split(" ")[0], x))
print('Par (1ª palabra, línea): {0}\n'.format(prdd.takeSample(False, 1)))

# Usando keyBy(f): Crea tuplas de los elementos del RDD usando f para obtener la clave.
nrdd = sc.parallelize(range(2,5))
prdd = nrdd.keyBy(lambda x: x*x)
prdd1 = nrdd.map(lambda x: (x,x*x))
print(prdd.collect())
print(prdd1.collect())

# zipWithIndex(): Zipea el RDD con los índices de sus elementos.
rdd = sc.parallelize(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 3)
prdd = rdd.zipWithIndex()
print(rdd.glom().collect())
print(prdd.collect())
# Este método dispara un Spark job cuando el RDD tiene más de una partición.

# zipWithUniqueId(): Zipea el RDD con identificadores únicos (long) para cada elemento.
# Los elementos en la partición k-ésima obtienen los ids k, n+k, 2*n+k,... siendo n = nº de particiones
# No dispara un trabajo Spark
rdd = sc.parallelize(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 3)
print("Particionado del RDD: {0}".format(rdd.glom().collect()))
prdd = rdd.zipWithUniqueId()
print(prdd.collect())

# Mediante un zip de dos RDDs
# Los RDDs deben tener el mismo número de particiones y el mismo número de elementos en cada partición
rdd1 = sc.parallelize(range(0, 5), 2)
rdd2 = sc.parallelize(range(1000, 1005), 2)
prdd = rdd1.zip(rdd2)
print(prdd.collect())

sc.stop()
