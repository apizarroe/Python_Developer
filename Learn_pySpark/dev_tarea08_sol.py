# A partir del fichero cite75_99.txt vuelve a obtener el número de citas por patente pero ahora usando DataFrames. 
# Ontén las tres patentes que más veces han sido citadas y el máximo, mínimo y media de citas de todas las patentes.

# Preguntas de esta tarea
# ¿Cuál es el número de la patente que vas veces ha sido citada?
# ¿Cuántas citas ha obtenido la patente que está en tercer lugar por número de citas?
# Indica, con tres cifras decimales, la media del número de citas por patente,

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from pyspark.sql import SparkSession
spark = SparkSession(sc)

rdd = sc.textFile("./datos/cite75_99.txt").filter(lambda x: '"CITING"' not in x).map(lambda l: l.split(","))
dfCitas = rdd.toDF(["Citante","Citada"]).cache()
grupoCitas = dfCitas.groupBy("Citada")
dfCuenta = grupoCitas.count().withColumnRenamed("count","Ncitas").cache()
dfCuenta.orderBy("Ncitas",ascending=False).show(3)
dfCuenta.describe("Ncitas").show()

sc.stop()
