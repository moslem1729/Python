def two_number_sum(array, target):
    potential_values = {}
    two_number = []
    for item in array:
        potential_value = target - item
        if potential_value in potential_values :
            two_number.append([item, potential_value])
        else:
            potential_values[item] = 1

    return two_number


array1 = [-4,1, 4, 2, 3, 7, -2, 9, 13]
print(two_number_sum(array1, 5))
