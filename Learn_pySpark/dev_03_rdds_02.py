import unittest

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

##########Acciones RDD
# reduce(op) combina los elementos de un RDD en paralelo, aplicando un operador
# El operador de reducción debe ser un monoide conmutativo (operador binario asociativo y conmutativo)
# Primero se realiza la redución a nivel de partición y luego se van reduciendo los valores intermedios
rdd = sc.parallelize(range(1,10))
print(rdd.glom().collect())
#Reduccion con una funcion lambda
p = rdd.reduce(lambda x,y: x*y)
print("1*2*3*4*5*6*7*8*9 = {0}".format(p))
#Reduccion con un operador predefinido
from operator import add
s = rdd.reduce(add)
print("1+2+3+4+5+6+7+8+9 = {0}".format(s))
#Prueba con un operador no conmutativo
p = rdd.reduce(lambda x,y: x-y) # r = 1-2-3-4-5-6-7-8-9 = -43
print("1-2-3-4-5-6-7-8-9 = {0}".format(p))
#No funciona con RDDS vacios
#sc.parallelize([]).reduce(add)

# fold(cero, op) versión general de reduce:
# Debemos proporcionar un valor inicial cero para el operador
# El valor inicial debe ser el valor identidad para el operador (p.e. 0 para suma; 1 para producto, o una lista vacía para concatenación de listas)
# Permite utilizar RDDs vacíos
# La función op debe ser un monoide conmutativo para garantizar un resultado consistente
# Comportamiento diferente a las operaciones fold de lenguajes como Scala
# El operador se aplica a nivel de partición (usando cero como valor inicial), y finalmente entre todas las particiones (usando cerode nuevo)
# Para operadores no conmutativos el resultado podría ser diferente del obtenido mediante un fold secuencial
rdd = sc.parallelize([list(range(1,5)), list(range(-10,-3)), ['a','b','c']])
print(rdd.glom().collect())
f = rdd.fold([], lambda x,y: x+y)
print(f)
rdd1 = sc.parallelize(range(7))
f1 = rdd1.fold(0, lambda x,y: x+y)
print(f1)
#Se puede hacer un fold de un RDD vacio
sc.parallelize([]).fold(0,add)

# aggregate(cero,seqOp,combOp): Devuelve una colección agregando los elementos del RDD usando dos funciones:
# seqOp - agregación a nivel de partición: se crea un acumulador por partición (inicializado a cero) y se agregan los valores de la partición en el acumulador
# combOp - agregación entre particiones: se agregan los acumuladores de todas las particiones
# Ambas agregaciones usan un valor inicial cero (similar al caso de fold).
# Versión general de reduce y fold
# La primera función (seqOp) puede devolver un tipo, U, diferente del tipo T de los elementos del RDD
# seqOp agregar datos de tipo T y devuelve un tipo U
# combOp agrega datos de tipo U
# cero debe ser de tipo U
# Permite devolver un tipo diferente al de los elementos del RDD de entrada.
# EJEMPLO01 Aggregate
l = [1,2,3,4,5,6,7,8]
rdd = sc.parallelize(l)
# acc es una tupla de tres elementos (List, Double, Int)
# En el primer elemento de acc (lista) le concatenamos los elementos del RDD al cuadrado
# en el segundo, acumulamos los elementos del RDD usando multiplicación
# y en el tercero, contamos los elementos del RDD
seqOp  = (lambda acc, val: (acc[0]+[val*val], 
                            acc[1]*val, 
                            acc[2]+1))
# Para cada partición se genera una tupla tipo acc
# En esta operación se combinan los tres elementos de las tuplas
combOp = (lambda acc1, acc2: (acc1[0]+acc2[0], 
                              acc1[1]*acc2[1], 
                              acc1[2]+acc2[2]))
a = rdd.aggregate(([], 1., 0), seqOp, combOp) 
print(a)
assert a[1] == 8.*7.*6.*5.*4.*3.*2.*1.
assert a[2] == len(l)
# EJEMPLO02 Aggregate
#Se implementa un ejemplo de prueba personalizado, para la funcion aggregate
arr = sc.parallelize(range(1,6))
print(arr.collect())
seqOp1 = (lambda acc,val: (acc[0]+[val+1],
                        acc[1]*val,
                        acc[2]+val))
cmbOp1 = (lambda acc1,acc2: (acc1[0]+acc2[0],
                        acc1[1]*acc2[1],
                        acc1[2]+acc2[2]))
abc = arr.aggregate(([],1.,0),seqOp1,cmbOp1)
print(abc)

# count() devuelve un entero con el número exacto de elementos del RDD
# countApprox(timeout, confidence=0.95) versión aproximada de count() que devuelve un resultado potencialmente incompleto en un tiempo máximo, incluso si no todas las tareas han finalizado. (Experimental).
# timeout es un entero largo e indica el tiempo en milisegundos
# confidence probabilidad de obtener el valor real. Si confidence es 0.90 quiere decir que si se ejecuta múltiples veces, se espera que el 90% de ellas se obtenga el valor correcto. Valor [0,1]
# countApproxDistinct(relativeSD=0.05) devuelve una estimación del número de elementos diferentes del RDD. (Experimental).
# relativeSD – exactitud relativa (valores más pequeños implican menor error, pero requieren más memoria; debe ser mayor que 0.000017).
rdd =  sc.parallelize([i % 20 for i in range(10000)], 16)
#print(rdd.collect())
print("Número total de elementos: {0}".format(rdd.count()))
print("Número de elementos distintos: {0}".format(rdd.distinct().count()))
print("Número total de elementos (aprox.): {0}".format(rdd.countApprox(1, 0.4)))
print("Número de elementos distintos (aprox.): {0}".format(rdd.countApproxDistinct(0.5)))

# countByValue() devuelve el número de apariciones de cada elemento del RDD como un mapa (o diccionario) de tipo clave/valor
# Las claves son los elementos del RDD y cada valor, el número de ocurrencias de la clave asociada al mismo
# EJEMPLO01 Cadena
rdd = sc.parallelize(list("abracadabra")).cache()
mimapa =  rdd.countByValue()
print(type(mimapa))
print(mimapa.items())
# EJEMPLO02 Numero
rddini = sc.parallelize(range(10))
rddcua = rddini.flatMap(lambda x: (x,x%3))
print(rddcua.collect())
#print(rddcua.collect())
mimapa001 = rddcua.countByValue()
print(mimapa001.items())

##########Acciones para obtener valores
#collect() devuelve una lista con todos los elementos del RDD
lista = rdd.collect()
print(lista)

# take(n) devuelve los n primeros elementos del RDD
# takeSample(withRep, n, [seed]) devuelve n elementos aleatorios del RDD
# withRep: si True, en la muestra puede aparecer el mismo elemento varias veces
# seed: semilla para el generador de números aleatorios
t = rdd.take(4)
print(t)
s = rdd.takeSample(False, 4)
print(s)

# top(n) devuelve una lista con los primeros n elementos del RDD ordenados en orden descendente
# takeOrdered(n,[orden]) devuelve una lista con los primeros n elementos del RDD en orden ascendente (opuesto a top), o siguiendo el orden indicado en la función opcional
rdd = sc.parallelize([8,4,2,9,3,1,10,5,6,7]).cache()
print("4 elementos más grandes: {0}".format(rdd.top(4)))
print("4 elementos más pequeños: {0}".format(rdd.takeOrdered(4)))
print("4 elementos más grandes: {0}".format(rdd.takeOrdered(4, lambda x: -x)))

sc.stop()