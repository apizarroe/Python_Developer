# A partir del fichero apat63_99.txt obtén y representa, por año de concesión ("GYEAR"), el número 
# de patentes cuyo primer inventor es de EEUU (código "US" en "COUNTRY"), usando un gráfico de barras. 
# Obtén también el número medio de patentes concedidas.
# Preguntas de esta tarea
# ¿Cuántas patentes has obtenido para el año 1966?
# ¿Cuál es la media?

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

# Se realiza la lectura del archivo apat63_99.txt
rdd = sc.textFile("./datos/apat63_99.txt")
from operator import add 
# Se toma 'rdd', se filtra por aquellos registros que son de "US"
# Se splitea cada linea del archivo
# Se forma un prdd (AÑO, 1), se realiza un reduceByKey con 'add' para calcular patentes por año
# Se ordena ascendentemente por AÑO, finalmente se cachea el prdd
yearNum = rdd.filter(lambda x: '"US"' in x).map(lambda x: x.split(",")).\
    map(lambda x: (x[1],1)).reduceByKey(add).sortByKey().cache()
# Se obtiene los numeros de patentes (por año) para calcular la media
media = yearNum.values().mean()
print("Media de patentes entre el año {0} y el año {1} = {2}".\
    format(yearNum.keys().min(),yearNum.keys().max(),media))

# Se realiza la grafica de barras #Patentes vs Años
years = yearNum.keys().collect()
numPats = yearNum.values().collect()
import numpy as np
import matplotlib.pyplot as plt
plt.gcf().clear()
yearsRange = np.arange(len(years))
plt.bar(years,numPats,align='center')
plt.xticks(yearsRange,years,fontsize=10,rotation=90)
plt.ylabel("N Patentes")
plt.show()


sc.stop()