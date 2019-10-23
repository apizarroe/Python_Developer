import pyspark
sc = pyspark.SparkContext(appName="myAppName")

cites = sc.textFile("cite75_99.txt")
header = cites.first()
cites = cites.filter(lambda x: x != header).map(lambda x: (x.split(",")[0],x.split(",")[1]))
#print(cites.take(10))
#[('3858241', '956203'), ('3858241', '1324234'), ('3858241', '3398406'), ('3858241', '3557384'), 
# ('3858241', '3634889'), ('3858242', '1515701'), ('3858242', '3319261'), ('3858242', '3668705'), 
# ('3858242', '3707004'), ('3858243', '2949611')]

# ¿Cuántas citas ha recibido la patente número 3986997?
prdd01 = cites.values().filter(lambda x: x == '3986997').count()
print("3986997 ha recibido {0} patentes".format(prdd01))

# ¿Cuántas citas ha recibido la patente número 4418284?
prdd01 = cites.values().filter(lambda x: x == '4418284').count()
print("4418284 ha recibido {0} patentes".format(prdd01))

# ¿Cuántas citas ha recibido la patente número 4314227?
prdd01 = cites.values().filter(lambda x: x == '4314227').count()
print("4314227 ha recibido {0} patentes".format(prdd01))

# ¿Cuántas citas ha recibido la patente número 3911418?
prdd01 = cites.values().filter(lambda x: x == '3911418').count()
print("3911418 ha recibido {0} patentes".format(prdd01))

# ¿Cuál es la patente que ha recibido más citas? Indica el número de patente.
from operator import add
prdd02 = cites.values().map(lambda x: (x,1)).reduceByKey(add).sortBy(lambda x: -x[1])
print(prdd02.take(1))

sc.stop()