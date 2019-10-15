import unittest

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

rdd = sc.parallelize(range(-5,5)) #Se paraleliza y se genera una lista con los numeros del -5 al 5
filtered_rdd = rdd.filter(lambda x: x >= 0) #Se filtran los datos que son mayores a 0
print(filtered_rdd.glom().collect()) #Se imprimen los datos resultantes particionados
print(filtered_rdd.collect()) #Se imprimen la lista de datos final

assert filtered_rdd.collect() == [0,1,2,3,4], "NO Se valida la ejecución" #Se realiza un Assert.

