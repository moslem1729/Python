# my_file = open("ttt.txt")
# content=my_file.read()
# my_file.close()
import pandas
# with open("C:/Users/moslem/Desktop/test1/test.txt") as my_file:
#     content = my_file.read()
#
# content += "\ntomato"
# with open("C:/Users/moslem/Desktop/test1/test.txt", "w") as my_file:
#     my_file.write(content)
#
# with open("C:/Users/moslem/Desktop/test1/test.txt", "a+") as my_file:
#     my_file.write("\ngarlic")
#     my_file.seek(10)
#     ccl=my_file.read()
#
# with open("C:/Users/moslem/Desktop/test1/test.txt") as my_file:
#     cc = my_file.read()
#
# print(ccl)
# print(cc)
# item = ""
# array = []
# for char in cc:
#     if char == "\n":
#         array.append(item)
#         item = ""
#     else:
#         item += char
# array.append(item)
#
# print(array)
df=pandas.read_csv("C:/Users/moslem/desktop/test1/supermarkets.csv")
df.set_index("ID",inplace=True)
first=[]
second=[]
third=[]
for item in df.Address:
    first.append(item[0:4])
    second.append(item[5:10])
    third.append(item[10:13])

print(first)
print(second)
print(third)

print(df)
