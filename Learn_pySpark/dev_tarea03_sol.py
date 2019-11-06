# Escribir un programa PySpark que, a partir del fichero apat63_99.txt, obtenga, para cada país de invención
#  (campo "COUNTRY" del fichero), el número medio de reivindicaciones (campo "CLAIMS" del fichero) de sus patentes.
# Preguntas de esta tarea
# ¿Cuál es el número medio de claims para España (código de país "ES")?
# ¿Cuál es el número medio de claims para Argentina (código de país "AR")?
# ¿Cuál es el número medio de claims para México (código de país "MX")?

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

# Se define una funcion toint para controlar los claim no numericos
def toint(nclaim):
    try:
        return int(nclaim)
    except:
        return (0)

# Se realiza la lectura del archivo apat63_99.txt
# Se realiza el filtrado de la primera linea (cabecera)
# Se forma un prdd ("COUNTRY","CLAIMS"), finalmente se cachea el prdd
rdd = sc.textFile("./datos/apat63_99.txt").filter(lambda l: "PATENT" not in l).\
    map(lambda x: (x.split(",")[4],toint(x.split(",")[8]))).cache()
# Se aplica combineByKey, para calcular la suma de los CLAIMS por COUNTRY, finalmente se cachea el prdd
sumCount = rdd.combineByKey(
                            (lambda x: (x, 1)),
                            (lambda x, y: (x[0]+y, x[1]+1)),
                            (lambda x, y: (x[0]+y[0], x[1]+y[1]))).cache()
# Se calcula la media de CLAIMS por COUNTRY
media = sumCount.mapValues(lambda v: float(v[0])/v[1]).sortByKey()
# Se realiza la busqueda de las llaves, para conocer la cantidad de media de CLAIMS
print(media.lookup('"ES"'))
print(media.lookup('"AR"'))
print(media.lookup('"MX"'))

sc.stop()
