import pyspark
sc = pyspark.SparkContext(appName="myAppName")

quijote = sc.textFile("quijote.txt")

palabrasrdd = quijote.flatMap(lambda x: x.split(" "))
# Se cuenta las lineas que llevan la cadena Quijote
filtro1 = palabrasrdd.filter(lambda l: "Quijote" in l).count()
# Se cuenta las lineas que llevan la cadena Sancho
filtro2 = palabrasrdd.filter(lambda l: "Sancho" in l).count()
# Se cuenta las lineas que llevan la cadena Rocinante
filtro3 = palabrasrdd.filter(lambda l: "Rocinante" in l).count()

print("Quijote: "+str(filtro1))
print("Sancho: "+str(filtro2))
print("Rocinante: "+str(filtro3))

