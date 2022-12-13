from unittest import result
from python.DataStructures.BST import Tree


def right_smaller_than(numbers):
    result=[]
    for i in range(len(numbers)-1):
        number_of_smaller_than=0
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[i]:
                number_of_smaller_than+=1
        result.append(number_of_smaller_than)
    result.append(0)

    return result

numbers=[8,5,11,-1,3,4,2]
print(right_smaller_than(numbers))
