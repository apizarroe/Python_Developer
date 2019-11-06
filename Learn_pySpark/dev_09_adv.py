# Trabajos, etapas y tareas
# Un programa Spark define un DAG conectando los diferentes RDDs

# Las transformaciones crean RDDs hijos a partir de RDDs padres
# Las acciones traducen el DAG en un plan de ejecución

# El driver envía un trabajo (job) para computar todos los RDDs implicados en la acción
# El job se descompone en una o más etapas (stages)
# Cada etapa está asociada a uno o más RDDs del DAG
# Las etapas se procesan en orden, lanzándose tareas (tasks) individuales que computan segmentos de los RDDs
# Pipelining: varios RDDs se pueden computan en una misma etapa si se verifica que:

# Los RDDs se pueden obtener de sus padres sin movimiento de datos (p.e. map), o bien
# si alguno de los RDDs se ha cacheado en memoria o disco
# En el interfaz web de Spark se muestran información sobre las etapas y tareas (más info: método toDebugString() de los RDDs)

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

# Acumuladores
# Permiten agregar valores desde los worker nodes, que se pasan al driver
# Útiles para contar eventos
# Solo el driver puede acceder a su valor
# Acumuladores usados en transformaciones de RDDs pueden ser incorrectos
# Si el RDD se recalcula, el acumulador puede actualizarse
# En acciones, este problema no ocurre
# Por defecto, los acumuladores son enteros o flotantes
# Es posible crear “acumuladores a medida” usando AccumulatorParam

from numpy.random import randint
npares = sc.accumulator(0)

def esPar(n):
    global npares
    if n%2 == 0:
        npares += 1

rdd = sc.parallelize(randint(100, size=10000))
rdd.foreach(esPar)
print("N pares: %d" % npares.value)

# Variables de broadcast
# Por defecto, todas las variables compartidas (no RDDs) son enviadas a todos los ejecutores
# Se reenvían en cada operación en la que aparezcan
# Variables de broadcast: permiten enviar de forma eficiente variables de solo lectura a los workers
# Se envían solo una vez

from operator import add
# dicc es una variable de broadcast
dicc=sc.broadcast({"a":"alpha","b":"beta","c":"gamma"})
rdd=sc.parallelize([("a", 1),("b", 3),("a", -4),("c", 0)])
reduced_rdd = rdd.reduceByKey(add).map(lambda x: (dicc.value[x[0]],x[1]))
print(reduced_rdd.collect())

# Trabajando a nivel de partición
# Una operación map se hace para cada elemento de un RDD
# Puede implicar operaciones redundantes (p.e. abrir una conexión a una BD)
# Puede ser poco eficiente
# Se pueden hacer map y foreach una vez por partición:
# Métodos mapPartitions(), mapPartitionsWithIndex() y foreachPartition()

nums = sc.parallelize([1,2,3,4,5,6,7,8,9], 2)
print(nums.glom().collect())

def sumayCuenta(iterador):
    sumaCuenta = [0,0]
    for i in iterador:
        sumaCuenta[0] += i
        sumaCuenta[1] += 1
    return sumaCuenta
    
print(nums.mapPartitions(sumayCuenta).glom().collect())

#####
def sumayCuentaIndex(index, it):
    return "Particion "+str(index), sumayCuenta(it)

print(nums.mapPartitionsWithIndex(sumayCuentaIndex).glom().collect())

#####
# import os
# import tempfile

# def f(iterator):
#     tempfich, _ = tempfile.mkstemp(dir=tempdir)
#     for x in iterator: 
#         os.write(tempfich, str(x)+'\t')
#     os.close(tempfich)
        
# tempdir = "/tmp/foreachPartition"
# if not os.path.exists(tempdir):
#     os.mkdir(tempdir)
#     nums.foreachPartition(f)


sc.stop()
