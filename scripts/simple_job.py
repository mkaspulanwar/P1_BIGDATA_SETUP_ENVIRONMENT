from pyspark.sql import SparkSession
spark = SparkSession.builder \
 .appName("SimpleJob") \
 .getOrCreate()
data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]
df = spark.createDataFrame(data, columns)
df.groupBy("category").sum("value").show()
spark.stop()