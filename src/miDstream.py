from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext


if __name__ == "__main__":
    sc = SparkContext(appName= "miDstream")
    sc.setLogLevel("ERROR")
    ssc= StreamingContext(sc, 3)

    #inputStream= ssc.socketTextStream("localhost",9999)
    inputStream= ssc.socketTextStream("host.docker.internal",9999)
    
    
    nuevoDStream = inputStream.map(lambda record: record.upper())
    
    print(f'inputStream: {inputStream}, nuevoDStream: {nuevoDStream}')
    nuevoDStream.pprint()

    ssc.start()
    ssc.awaitTermination()