import unittest

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

##########Transformaciones RDD
#filter(func) filtra los elementos de un RDD
rdd = sc.parallelize(range(-5,5)) #Se paraleliza y se genera una lista con los numeros del -5 al 5
filtered_rdd = rdd.filter(lambda x: x >= 0) #Se filtran los datos que son mayores a 0
print(filtered_rdd.glom().collect()) #Se imprimen los datos resultantes particionados
print(filtered_rdd.collect()) #Se imprimen la lista de datos final
assert filtered_rdd.collect() == [0,1,2,3,4], "NO Se valida la ejecución" #Se realiza un Assert.

#map(func) aplica una función a los elementos de un RDD
#Añade 1 a cada elemento del RDD
def add1(x):
    return (x+1)
#Se toma el rdd: filtered_rdd y se aplica la funcion add1 y luego (x, x*x)
squared_rdd = (filtered_rdd             
                .map(add1)              #Añade 1 a cada elemento del RDD
                .map(lambda x: (x,x*x)))    #Para cada elemento, obten una tupla (x, x*x)
print(squared_rdd.collect())
assert squared_rdd.collect() == [(1,1),(2,4),(3,9),(4,16),(5,25)] #Se realiza un Assert

#flatMap(func) igual que map, pero “aplana” la salida
#Se toma el rdd: filtered_rdd y se aplica la funcion add1 y luego (x, x*x) "aplanado"
squaredflat_rdd = (filtered_rdd.map(add1).flatMap(lambda x: (x, x*x)))
print(squaredflat_rdd.collect())
assert squaredflat_rdd.collect() == [1,1,2,4,3,9,4,16,5,25] #Se realiza el Assert.

# sample(withReplacement, fraction, seed=None) devuelve una muestra del RDD
# withReplacement - si True, cada elemento puede aparecer varias veces en la muestra
# fraction - tamaño esperado de la muestra como una fracción del tamaño del RDD
# sin reemplazo: probabilidad de seleccionar un elemento, su valor debe ser [0, 1] (False)
# con reemplazo: número esperado de veces que se escoge un elemento, su valor debe ser >= 0 (True)
# seed - semilla para el generador de números aleatorios
srdd1 =  squaredflat_rdd.sample(False, 0.5)
srdd2 =  squaredflat_rdd.sample(True, 2)
srdd3 =  squaredflat_rdd.sample(False, 0.8)
print('s1={0}\ns2={1}\ns3={2}'.format(srdd1.collect(),srdd2.collect(),srdd3.collect()))

# distinct() devuelve un nuevo RDD sin duplicados
distinct_rdd = squaredflat_rdd.distinct() #Se llama a la funcion distinct.
print(distinct_rdd.collect())

# groupBy(func) devuelve un RDD con los datos agrupados en formato clave/valor,
# usando una función para obtener la clave
# EJEMPLO01 de del groupBy
grouped_rdd = distinct_rdd.groupBy(lambda x: x%3)
#Se muestran los arreglos arreglos por cada valor que toma 'y' 
print(grouped_rdd.collect())
#Se muestran los datos agrupados y ordenados
print([(x,sorted(y)) for (x,y) in grouped_rdd.collect()])
# EJEMPLO02 de del groupBy
rdd1 = sc.parallelize(range(30))
g_rdd = rdd1.groupBy(lambda x: x%4)
#Se muestran los datos agrupados y ordenados
print([(x,sorted(y)) for (x,y) in g_rdd.collect()])

##########Transformaciones sobre dos RDDs
#rdda.union(rddb) devuelve un RDD con los datos de los dos de partida
rdda = sc.parallelize(['a','b','c'])
rddb = sc.parallelize(['c','d','e'])
#Se realiza la operacion union de conjuntos entre el rdda y rddb.
rddu = rdda.union(rddb)
print(rddu.collect())
assert rddu.collect() == ['a','b','c','c','d','e']

#rdda.intersection(rddb) devuelve un RDD con los datos comunes en ambos RDDs
#Se realiza la operacion interseccion de conjuntos entre el rdda y rddb.
rddi = rdda.intersection(rddb)
print(rddi.collect())
assert rddi.collect() == ['c']

# rdda.subtract(rddb) devuelve un RDD con los datos del primer RDD menos los del segundo
#Se realiza la operacion sustraccion de conjuntos entre el rdda y rddb.
rdds = rdda.subtract(rddb)
print(rdds.collect())
assert rdds.collect() == ['a','b']

#rdda.cartesian(rddb) producto cartesiano de ambos RDDs (operación muy costosa)
#Esto se debe a que se deben copiar todos los elementos en cada una de las particiones
rddc = rdda.cartesian(rddb)
print(rddc.collect())
assert rddc.collect() == [('a','c'),('a','d'),('a','e'),('b','c'),('b','d'),('b','e'),('c','c'),('c','d'),('c','e')]

sc.stop()