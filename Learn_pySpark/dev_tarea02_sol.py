import pyspark
sc = pyspark.SparkContext(appName="myAppName")

###############SOLUCION DE PROFESOR
from operator import add
rdd = sc.textFile("cite75_99.txt").filter(lambda l: '"CITING","CITED"' not in l).map(lambda l: (l.split(",")[1],1)).\
    reduceByKey(add).cache()
rdd2 = rdd.sortByKey()
print(rdd2.lookup('3986997'))
print(rdd2.lookup('4418284'))
print(rdd2.lookup('4314227'))
print(rdd2.lookup('3911418'))
rdd1 = rdd.map(lambda x: (x[1],x[0])).sortByKey(False)
print(rdd1.take(1))
#Otra opcion es invertir el orden de los campos y usar el countByKey()

sc.stop()