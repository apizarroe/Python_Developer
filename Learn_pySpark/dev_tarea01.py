import pyspark
sc = pyspark.SparkContext(appName="myAppName")

quijote = sc.textFile("quijote.txt")

palabrasrdd = quijote.flatMap(lambda x: x.split(" "))
filtro1 = palabrasrdd.filter(lambda l: "Quijote" in l).count()
filtro2 = palabrasrdd.filter(lambda l: "Sancho" in l).count()
filtro3 = palabrasrdd.filter(lambda l: "Rocinante" in l).count()

print("Quijote "+str(filtro1))
print("Sancho "+str(filtro2))
print("Rocinante "+str(filtro3))

