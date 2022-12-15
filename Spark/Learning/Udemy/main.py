from pyspark.sql import SparkSession
from pyspark.sql.types import (StructField, StringType,
                               IntegerType, StructType)

spark = SparkSession.builder.appName('basics').getOrCreate()

data_schema = [StructField('age', IntegerType(), True),
               StructField('name', StringType(), True)]

final_struc = StructType(fields=data_schema)

df = spark.read.json('people.json', final_struc)

df.show()
df.printSchema()
print(df.columns)
df.describe().show()
