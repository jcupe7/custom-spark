from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    sc = SparkContext(appName= "miDstream")
    sc.setLogLevel("ERROR")
    ssc= StreamingContext(sc, 10)

    inputStream= ssc.socketTextStream("localhost",9999)

    nuevoDStream = inputStream.map(lambda record: record.upper())
    nuevoDStream.pprint()

    ssc.start()
    ssc.awaitTermination()