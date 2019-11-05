import pyspark
sc = pyspark.SparkContext(appName="myAppName")

rdd = sc.textFile("apat63_99.txt")
from operator import add 
yearNum = rdd.filter(lambda x: '"US"' in x).map(lambda x: x.split(",")).\
    map(lambda x: (x[1],1)).reduceByKey(add).sortByKey().cache()
media = yearNum.values().mean()
print("Media de patentes entre el año {0} y el año {1} = {2}".format(yearNum.keys().min(),yearNum.keys().max(),media))

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