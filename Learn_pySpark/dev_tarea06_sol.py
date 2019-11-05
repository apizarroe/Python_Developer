import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from operator import add

info = sc.sequenceFile("./salida/apat63_99-seq").map(lambda x: (x[1].split(",")[0],(x[0],x[1].split(",")[1])))
num_citas = sc.textFile("cite75_99.txt").filter(lambda x: '"CITING"' not in x).map(lambda x: (x.split(",")[1],1)).\
    reduceByKey(add)
total = info.fullOuterJoin(num_citas)
#print(total.take(5))
print("Resultado")
print(total.filter(lambda x: x[0] == '5526839').collect())

sc.stop()