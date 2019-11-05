import pyspark
sc = pyspark.SparkContext(appName="myAppName")

##########Transformación de Pair RDDs
##########Transformaciones de agregación
# reduceByKey(func)/foldByKey(func)
# Devuelven un RDD, agrupando los valores asociados a la misma clave mediante func
# Similares a reduce y fold sobre RDDs simples
from operator import add
prdd = sc.parallelize([('a',2),('b',5),('a',8),('b',6),('b',2)]).cache()
redrdd = prdd.reduceByKey(add)
print(redrdd.collect())

# groupByKey() agrupa valores asociados a misma clave
# Operación muy costosa en comunicaciones
# Mejor usar operaciones de reducción
grouprdd = prdd.groupByKey()
print(grouprdd.collect())
lista = [(k,list(v)) for k,v in grouprdd.collect()]
print(lista)

# combineByKey(createCombiner(func1), mergeValue(func2), mergeCombiners(func3))
# Método general para agregación por clave, similar a aggregate
# Especifica tres funciones:
# createCombiner al recorrer los elementos de cada partición, si nos encontramos una clave nueva se crea un acumulador y se inicializa con func1
# mergeValue mezcla los valores de cada clave en cada partición usando func2
# mergeCombiners mezcla los resultados de las diferentes particiones mediante func3
# Los valores del RDD de salida pueden tener un tipo diferente al de los valores del RDD de entrada.
# Para cada clave, obten una tupla que tenga la suma y el número de valores
print("Esto tiene el prdd")
print(prdd.take(10))
sumCount = prdd.combineByKey(
                            (lambda x: (x, 1)),
                            (lambda x, y: (x[0]+y, x[1]+1)),
                            (lambda x, y: (x[0]+y[0], x[1]+y[1])))
print(sumCount.collect())
# Con el RDD anterior, obtenemos la media de los valores
m = sumCount.mapValues(lambda v: float(v[0])/v[1])
print(m.collect())

##########Transformaciones sobre claves o valores
# keys() devuelve un RDD con las claves
# values() devuelve un RDD con los valores
# sortByKey() devuelve un RDD clave/valor con las claves ordenadas
print("RDD completo: {0}".format(prdd.collect()))
print("RDD con las claves: {0}".format(prdd.keys().collect()))
print("RDD con los valores: {0}".format(prdd.values().collect()))
print("RDD con las claves ordenadas: {0}".format(prdd.sortByKey().collect()))

# mapValues(func) devuelve un RDD aplicando una función sobre los valores
# flatMapValues(func) devuelve un RDD aplicando una función sobre los valores y “aplanando” la salida
mapv = prdd.mapValues(lambda x: (x, 10*x))
print(mapv.collect())
fmapv = prdd.flatMapValues(lambda x: (x, 10*x))
print(fmapv.collect())

##########Transformaciones sobre dos RDDs clave/valor
#join/leftOuterJoin/rightOuterJoin/fullOuterJoin realizan inner/outer/full joins entre los dos RDDs
rdd1 = sc.parallelize([("a", 2), ("b", 5), ("a", 8), ("a", 3)]).cache()
rdd2 = sc.parallelize([("c", 7), ("a", 1), ("a", 6)]).cache()
#JOIN RDDs (Inner Join)
rdd3 = rdd1.join(rdd2)
print(rdd3.collect())
#JOIN LeftOuter RDDs
rdd3 = rdd1.leftOuterJoin(rdd2)
print(rdd3.collect())
#JOIN RightOuter RDDs
rdd3 = rdd1.rightOuterJoin(rdd2)
print(rdd3.collect())
#JOIN FullOuter RDDs
rdd3 = rdd1.fullOuterJoin(rdd2)
print(rdd3.collect())

#subtractByKey elimina elementos con una clave presente en otro RDD
rdd3 = rdd1.subtractByKey(rdd2)
print(rdd3.collect())

#cogroup agrupa los datos que comparten la misma clave en ambos RDDs
#muy costosa pues todos los valores deben ser enviadas entre los nodos
rdd3 = rdd1.cogroup(rdd2)
print(rdd3.collect())
#Los valores asociados a las llaves se muestran en una lista de listas
map = rdd3.mapValues(lambda v: [list(l) for l in v]).collectAsMap()
print(map)

##########Acciones sobre RDDs clave/valor
# collectAsMap() obtiene el RDD en forma de mapa
prdd = sc.parallelize([("a", 7), ("b", 5), ("a", 8), ("c", 4)]).cache()
rddMap = prdd.collectAsMap()
print(rddMap)

# countByKey() devuelve un mapa indicando el número de ocurrencias de cada clave
countMap = prdd.countByKey()
print(countMap)

# lookup(key) devuelve una lista con los valores asociados con una clave
listA = prdd.lookup('a')
print(listA)

sc.stop()
