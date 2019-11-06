# Funciones de estadística descriptiva implementadas en Spark
# Método                Descripción
# stats()               Resumen de estadísticas
# mean()                Media aritmética
# sum(), max(), min()	Suma, máximo y mínimo
# variance()            Varianza de los elementos
# sampleVariance()      Varianza de una muestra
# stdev()               Desviación estándar
# sampleStdev()         Desviación estándar de una muestra
# histogram()           Histograma

import pyspark
sc = pyspark.SparkContext(appName="myAppName")

import numpy as np
# Un RDD con datos aleatorios de una distribución normal
nrdd = sc.parallelize(np.random.normal(size=10000)).cache()
# Resumen de estadísticas
sts = nrdd.stats()
print("Resumen de estadísticas:\n {0}\n".format(sts))

from math import fabs
# Filtra outliers
stddev = sts.stdev()
avg = sts.mean()
frdd = nrdd.filter(lambda x: fabs(x - avg) < 3*stddev).cache()
print("Número de outliers: {0}".format(sts.count() - frdd.count()))

#import base64
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
#import StringIO
#def show(p):
    #img = StringIO.StringIO()
    #p.savefig(img, format='svg')
    #img.seek(0)
    #print "%html <div style='width:600px'>" + img.buf + "</div>"
# Obtiene un histograma con 10 grupos
x,y = frdd.histogram(10)
# Limpia la gráfica
plt.gcf().clear()
plt.bar(x[:-1], y, width=0.6)
plt.xlabel(u'Valores')
plt.ylabel(u'Número de ocurrencias')
plt.title(u'Histograma')
plt.show()

sc.stop()