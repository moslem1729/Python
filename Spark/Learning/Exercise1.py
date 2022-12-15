from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import (FloatType)

# book_schema = [StructField('UserID', StringType(), True),
#                StructField('USERNAME', StringType(), True),
#                StructField('Location', StringType(), True),
#                StructField('Age', IntegerType(), True)]
# book_struc = StructType(fields=book_schema)
sp = SparkSession.builder.appName('exercise').getOrCreate()

books_rating = sp.read.csv('BooksRating-CSV/Book-Ratings.csv', sep=';', header=True)

books_rating = books_rating.withColumn("rate", col("rate").cast(FloatType()))

books = sp.read.csv('BooksRating-CSV/Books.csv', sep=';', header=True)

books_avg_rate = books_rating.groupBy(books_rating['ISBN']).avg('rate')

users = sp.read.csv('BooksRating-CSV/Users.csv', sep=';', header=True)

result = users.join(books_rating, books_rating['userid'] == users["UserID"])

result = result.select(["USERNAME", "isbn", "rate"])

result = result.join(books, books['ISBN'] == result['isbn'])

books_avg_rate = books_avg_rate.join(books, books_avg_rate['isbn'] == books['isbn'])

books_avg_rate.select(["BookTitle", "avg(rate)"])

result = result.select(["USERNAME", "BookTitle", "rate"])

result = result.join(books_avg_rate, books_avg_rate["BookTitle"] == result["BookTitle"])

# result = result.select(["USERNAME", "BookTitle", "rate", "avg(rate)"])
result.show()

# books_avg_rate.join(books, books['ISBN'] == books_avg_rate['ISBN']).show()
