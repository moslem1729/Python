def first_duplicate_value(array):
    number_of_value = {}
    for item in array:
        if item in number_of_value:
            return item
        else:
            number_of_value[item] = 1
    return -1


def first_duplicate_value_set(array):
    seen = set()
    for item in array:
        if item in seen:
            return item
        seen.add(item)
    return -1


def first_duplicate_value_where_all_the_values_are_in_range_1_n(array):
    for value in array:
        abs_value = abs(value)
        if array[abs_value-1]<0:
            return abs_value
        array[abs_value-1]*=-1
    return -1


arr = [2, 1, 5, 3, 4, 3, 4]
print(first_duplicate_value(arr))
print(first_duplicate_value_set(arr))
print(first_duplicate_value_where_all_the_values_are_in_range_1_n(arr))
