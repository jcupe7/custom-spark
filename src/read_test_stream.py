from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

ssc = StreamingContext(spark.sparkContext, batchDuration=1)

kafkaParams = {
    "bootstrap.servers": "localhost:9092",
    "auto.offset.reset": "largest",
    "group.id": "spark-streaming-kafka-demo"
}

kafkaStream = KafkaUtils.createDirectStream(
    ssc,
    topics=["test_topic"],
    kafkaParams=kafkaParams
)

lines = kafkaStream.map(lambda x: x[1])
words = lines.flatMap(lambda x: x.split(" "))
wordCounts = words.countByValue()
wordCounts.pprint()

ssc.start()
ssc.awaitTermination()
