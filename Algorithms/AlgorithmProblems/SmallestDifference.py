def smallest_difference(array1, array2):
    helper_array = [array1[0], array2[0]]
    for item1 in array1:
        for item2 in array2:
            if abs(item2 - item1) < abs(helper_array[0] - helper_array[1]):
                helper_array[0] = item1
                helper_array[1] = item2

    return helper_array


def smallest_difference_sort(array_one, array_two):
    array_one.sort()
    array_two.sort()
    index_one = 0
    index_two = 0
    smallest = float("inf")
    current = float("inf")
    smallest_pair = []
    while index_one < len(array_one) and index_two < len(array_two):
        first_num = array_one[index_one]
        second_num = array_two[index_two]
        if first_num < second_num:
            current = second_num - first_num
            index_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            index_two += 1
        else:
            return [first_num, second_num]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair


array11 = [10, 20, 28, 3, 4, 9]
array22 = [26, 134, 11, 17, 9]
print(smallest_difference_sort(array11, array22))
print(smallest_difference(array11, array22))
