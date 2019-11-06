# Elemento básico: DataFrames
# Colección distribuida de datos organizada en columnas con nombre
# Conceptualmente equivalente a una tabla en una BD o a un dataframe en R o Python Pandas
# Al igual que los RDDs son inmutables y lazy
# Desarrollados dentro de Spark SQL
# Permite acceder a los datos mediante consultas SQL
# Sustitutos de los RDDs en general
# DataSet: nuevo tipo de datos añadido en Spark 1.6
# Intenta proporcionar los beneficios de los RDDs con las optimizaciones que proporciona el motor de ejecución Tungsten de Spark SQL.
# Sólo disponible en Scala y Java
# En Java y Scala, un DataFrame es un DataSet de objetos de tipo Row

# Creación de DataFrames
# Varias formas:
# A partir de un RDD de listas/tuplas
# A partir de un RDD de objetos Row
# A partir de ficheros JSON
# A partir de otros almacenamientos (Parquet, Hive,…)

# DataFrame a partir de un RDD de listas/tuplas
# A partir de un fichero, se crea un RDD de listas que se convierte en un DataFrame.
# La creación del DataFrame se puede hacer de varias formas:
# Infiriendo el esquema
# Indicando el esquema de forma explícita

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
spark = SparkSession(sc)

# DataFrame a partir de un RDD de listas/tuplas infiriendo el esquema
# Leemos el fichero apat63_99.txt.
rdd = sc.textFile("./datos/apat63_99.txt").cache()
# Le quitamos la cabecera y lo convertimos en un RDD de listas
rddSplit = rdd.filter(lambda l: not l.startswith('"PATENT"'))\
              .map(lambda l: l.split(",")[0:16])
# Obtengo la cabecera como una lista de nombres (sin comillas dobles)
cabecera = [c.strip('"') for c in rdd.take(1)[0].split(",")[0:16]]
print(cabecera)
rdd.unpersist()
rddSplit.cache()

# Dos formas de crear el DataFrame
# 1. A partir del método createDataFrame de sqlContext
sqlContext = SQLContext(sc)
dfInfer1 = sqlContext.createDataFrame(rddSplit, cabecera)
# 2. A partir del método toDF del RDD
dfInfer2 = rddSplit.toDF(cabecera)
dfInfer1.show(10)
dfInfer2.show(10)

# Esquema de la tabla
dfInfer2.printSchema()

# Los tipos de datos no se han inferido de forma correcta
# Para que los tipos se infieran correctamente, podemos partir de un RDD de listas con los tipos correctos para cada campo.
# Convierto cambio el tipo de los datos del RDD de listas
def toIntSafe(inval):
  try:
    return int(inval)
  except ValueError:
    return 0
    
def toFloatSafe(inval):
  try:
    return float(inval)
  except ValueError:
    return 0.0

# Dejo todos los campos como Strings, menos el campo 8 (CLAIMS) que lo pongo como entero
# y el campo 15 (GENERAL) que lo pongo como float
rddTipos = rddSplit.map(lambda l: (l[0], 
                                   l[1],
                                   l[2], 
                                   l[3], 
                                   l[4].strip('"'), 
                                   l[5].strip('"'), 
                                   l[6], 
                                   l[7], 
                                   toIntSafe(l[8]),
                                   l[9],
                                   l[10], 
                                   l[11], 
                                   l[12], 
                                   l[13], 
                                   l[14], 
                                   toFloatSafe(l[15])))
rddTipos.cache()

dfInfer3 = sqlContext.createDataFrame(rddTipos, cabecera)
dfInfer3.printSchema()
dfInfer3.show(10)

# DataFrame a partir de un RDD de listas/tuplas indicando el esquema de forma explícita
# Defino el esquema para los elementos de la tabla usando un StructType de StructField
# StructType: Permite definir un esquema para el DataFrame a partir de una lista de StructFields
# StructField: Definen el nombre y tipo de cada columna, así como si es nullable o no
from pyspark.sql.types import *
# Defino el esquema para los elementos de la tabla
# StructType -> Permite definir un esquema para el DF a partir de una lista de StructFields
# StructField -> Definen el nombre y tipo de cada columna, así como si es nullable o no (campo True)
postSchema = StructType([
  StructField(cabecera[0], StringType(), False),
  StructField(cabecera[1], StringType(), True),
  StructField(cabecera[2], StringType(), True),
  StructField(cabecera[3], StringType(), True),
  StructField(cabecera[4], StringType(), True),
  StructField(cabecera[5], StringType(), True),
  StructField(cabecera[6], StringType(), True),
  StructField(cabecera[7], StringType(), True),
  StructField(cabecera[8], IntegerType(), True),
  StructField(cabecera[9], StringType(), True),
  StructField(cabecera[10], StringType(), True),
  StructField(cabecera[11], StringType(), True),
  StructField(cabecera[12], StringType(), False),
  StructField(cabecera[13], StringType(), True),
  StructField(cabecera[14], StringType(), True),
  StructField(cabecera[15], FloatType(), True)
  ])
# Creo el DataFrame
dfSchema = sqlContext.createDataFrame(rddTipos, postSchema).cache()
rddTipos.unpersist()
dfSchema.printSchema()
dfSchema.show(10)

# DataFrame a partir de un RDD de objetos Row
# Row Representa una fila de datos en un DataFrame
from pyspark.sql import Row
# Convierto el RDD de listas en un RDD de objetos Row
rddRows = rddSplit.map(lambda l: Row(Patent = l[0], 
                                     Gyear = l[1], 
                                     Gdate = l[2], 
                                     Appyear = l[3],
                                     Country = l[4],
                                     Postate = l[5],
                                     Assignee = l[6], 
                                     Asscode = l[7],
                                     Claims = toIntSafe(l[8]),
                                     Nclass = l[9], 
                                     Cat = l[10], 
                                     Subcat = l[11], 
                                     Cmade = l[12],
                                     Creceive = l[13],
                                     Ratiocit = l[14],
                                     General = toFloatSafe(l[15])))
# El esquema se infiere de los tipos
dfRows = sqlContext.createDataFrame(rddRows)
print("Esquema de la tabla en árbol")
dfRows.printSchema()
print("Nombres de las columnas\n{0}\n".
      format(dfRows.columns))
print("Tipos de las columnas\n{0}\n".
      format(dfRows.dtypes))
rddSplit.unpersist()
dfRows.show(10)

# Conversion de un DataFrame en un RDD de objetos Row
# Permite convertir un DataFrame en un RDD
rddRows2 = dfSchema.rdd
print("Muestra un elemento del nuevo RDD")
print(rddRows2.take(1))
print("Aplicamos un map al RDD")
print(rddRows2.map(lambda r: (r.COUNTRY, r.PATENT)).take(1))

# DataFrame a partir de un fichero JSON
dfJson = sqlContext.read.json("./datos/gente.json")
dfJson.show()

# Guardar el DataFrame como fichero JSON
dfSchema.write.json("./salida/apat63_99-json")

##### Operaciones básicas
##### Selección y eliminación de columnas
dfParcial = dfSchema.select("PATENT", "GYEAR", "COUNTRY", "CLAIMS")
dfParcial.show(10)
print("El objeto dfParcial es de tipo {0}".format(type(dfParcial)))
dfSchema.unpersist()
dfParcial.cache()
# También es posible crear objetos de tipo Column
colPatent = dfParcial["PATENT"]
colCountry = dfParcial.COUNTRY
print("El objeto colPatent es de tipo {0}".format(type(colPatent)))
print("El objeto colCountry es de tipo {0}".format(type(colCountry)))
# Y crear un DataFrame a partir de objetos Column, renombrando columnas
dfParcial2 = dfParcial.select(colPatent.alias("Patente"), colCountry.alias("País"), dfParcial.GYEAR.alias("Año"))
dfParcial2.show()
# Se pueden eliminar columnas
dfParcial3 = dfParcial.drop("CLAIMS")
dfParcial3.show(10)

##### Filtrado
# Patentes con CLAIMS > 0
dfClaims = dfParcial.where('CLAIMS > 0')
print("Número de patentes con reivindicaciones: {0}\n".\
       format(dfClaims.count()))
dfClaims.show(1)
# Patentes con inventor español
dfEsp = dfParcial.filter(colCountry.like('ES'))
print("Número de patentes con inventor español: {0}\n".\
       format(dfEsp.count()))
dfEsp.show(1)

##### Ordenación y agrupamiento
dfParcial.orderBy('CLAIMS', ascending=False).show(10)
grupoPorPais = dfParcial.groupBy('COUNTRY')
print(type(grupoPorPais))
print("Número de patentes por país")
grupoPorPais.count().orderBy('count', ascending=False).show()
print("Media de reivindicaciones por país")
grupoPorPais.avg('CLAIMS').orderBy('COUNTRY').show()

#####Joins
dfEsp80 = dfEsp.where('int(GYEAR) > 1979 and int(GYEAR) < 1990')
dfPatYear = dfEsp80.select(dfEsp80.PATENT.alias("Patente"), dfEsp80["GYEAR"].alias("Año"))
dfPatYear.show(5)
dfPatCountry = dfEsp80.select(dfEsp80.COUNTRY.alias("País"), dfEsp80.PATENT.alias("Patente"))
dfPatCountry.show(5)
dfPatYear.join(dfPatCountry, "Patente", "inner").show(5)

##### Funciones escalares y agregados
# Spark ofrece un ámplio abanico de funciones para operar con los DataFrames:
# Funciones matemáticas: abs, log, hypot, etc.
# Operaciones con strings: lenght, concat, etc.
# Operaciones con fechas: year, date_add, etc.
# Operaciones de agregación: min, max, count, avg, sum, sumDistinct, stddev, variance, kurtosis, skewness, first, last, etc.

# Obtener el máximo, mínimo, media y desviación estándard de las reivindicaciones de las patentes españolas
from pyspark.sql.functions import *
dfEsp.select(max("CLAIMS"), min("CLAIMS"),avg("CLAIMS"),stddev("CLAIMS")).show()

# Otra forma de hacer lo mismo
dfEsp.describe("CLAIMS").show()

##### Consultas SQL
# Registra la tabla para usar SQL
dfParcial.registerTempTable("patentinfo")
sqlContext.sql("SELECT COUNTRY,CLAIMS FROM patentinfo WHERE CLAIMS >= 100").show()

##### UDFs: Funciones definidas por el usuario
from pyspark.sql.functions import udf
from pyspark.sql.types import BooleanType
esPar = udf(lambda n: not n%2, BooleanType())
print("Información sobre si el número de reivindicaciones es par o impar.")
dfParcial.select(dfParcial.PATENT, dfParcial.CLAIMS, esPar(dfParcial.CLAIMS).alias("Par?")).\
  orderBy(dfParcial.CLAIMS, ascending=False).show()

sc.stop()


