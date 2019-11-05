import pyspark
sc = pyspark.SparkContext(appName="myAppName")

def toint(nclaim):
    try:
        return int(nclaim)
    except:
        return (0)

rdd = sc.textFile("apat63_99.txt").filter(lambda l: "PATENT" not in l).\
    map(lambda x: (x.split(",")[4],toint(x.split(",")[8]))).cache()

sumCount = rdd.combineByKey(
                            (lambda x: (x, 1)),
                            (lambda x, y: (x[0]+y, x[1]+1)),
                            (lambda x, y: (x[0]+y[0], x[1]+y[1]))).cache()

media = sumCount.mapValues(lambda v: float(v[0])/v[1]).sortByKey()
print(media.lookup('"ES"'))
print(media.lookup('"AR"'))
print(media.lookup('"MX"'))

sc.stop()
