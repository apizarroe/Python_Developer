# Escribir un programa Scala Spark que, a partir de los ficheros cite75_99.txt y apat63_99-seq, obtenga, para 
# cada patente, el país, el año y el número de citas.
# Utilizar un full outer join para unir, por el campo común (el número de patente) los RDDs asociados a ambos ficheros.
# Preguntas de esta tarea
# ¿Cuál es el año y el número de citas correspondientes a la patente número 5526839?
import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from operator import add
# Se realiza la lectura del archivo apat63_99.txt
# Se construye un prdd ('PATENTE', ('COUNTRY,AÑO'))
info = sc.sequenceFile("./salida/apat63_99-seq").map(lambda x: (x[1].split(",")[0],(x[0],x[1].split(",")[1])))
# Se realiza la lectura del archivo cite75_99.txt
# Se realiza el filtrado de la primera linea (cabecera)
# Se construye un prdd ('CITADO', 1)
# Se realiza un reduceByKey con 'add' a los valores
num_citas = sc.textFile("./datos/cite75_99.txt").filter(lambda x: '"CITING"' not in x).\
    map(lambda x: (x.split(",")[1],1)).reduceByKey(add)
# Se realiza aplica fullOuterJoin entre info y num_citas, para obtener un prrd (PATENTE, (('COUNTRY,AÑO'), #CITAS))
total = info.fullOuterJoin(num_citas)
print("Resultado")
# Se realiza el filtrado para encontrar la patente requerida
print(total.filter(lambda x: x[0] == '5526839').collect())

sc.stop()