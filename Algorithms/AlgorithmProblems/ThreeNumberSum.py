from operator import le
from turtle import right


def two_number_sum(array, target):
    potential_values = {}
    two_number = []
    for item in array:
        potential_value = target - item
        if potential_value in potential_values:
            two_number.append([potential_value, item])
        else:
            potential_values[item] = 1

    return two_number


def three_number_sum(array, target):
    three_number = []
    for index,item in enumerate(array):
        two_potential_numbers = []
        the_potential_sum = target - item
        new_array = array[index+1:]
        if len(new_array)>1:
            two_potential_numbers = two_number_sum(new_array, the_potential_sum)
        else:
            break
        if len(two_potential_numbers) > 0:
            for values in two_potential_numbers:
                three_number.append([item, values[0], values[1]])
    return three_number


def three_number_sum_another_solution(array,target):
    array.sort()
    triplets=[]
    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left<right:
            current_sum=array[i]+array[left]+array[right]
            if current_sum==target:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif current_sum<target:
                left+=1
            elif current_sum>target:
                right-=1
    return triplets

array1 = [12,3,1,2,-6,5,-8,6]

print(three_number_sum_another_solution(array1,0))
print(three_number_sum(array1,0))
