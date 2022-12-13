from pyspark import SparkContext

sc = SparkContext('local[*]', 'example')

nums = [1, 2, 3, 4, 5, 5, 6, 6, 1, 2, 1, 4]

rdd = sc.parallelize(nums)
print(rdd.take(5))
