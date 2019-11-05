import pyspark
sc = pyspark.SparkContext(appName="myAppName")
import os
os.system('rmdir /S /Q salida\\apat63_99-seq')

rdd = sc.textFile("apat63_99.txt")
prdd = rdd.filter(lambda l: not l.startswith('"PATENT"')).map(lambda l: l.split(",")).\
    map(lambda lista: (lista[4].strip('"'), lista[0]+","+lista[1]))
print(prdd.take(2))
prdd.saveAsSequenceFile("./salida/apat63_99-seq")

prdd2 = sc.sequenceFile("./salida/apat63_99-seq")
print(prdd2.countByKey()['US'])

sc.stop()