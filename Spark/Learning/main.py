from pyspark import SparkContext

sc = SparkContext('local[*]', 'Word Count Example')

books_rating = sc.textFile(r'BooksRating-CSV/Book-Ratings.csv', 8)
books = sc.textFile(r'BooksRating-CSV/Books.csv', 8)
users = sc.textFile(r'BooksRating-CSV/Users.csv', 8)

