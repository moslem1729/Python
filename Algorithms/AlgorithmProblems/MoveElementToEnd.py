def move_element_to_end(array, element):
    for i in range(len(array)):
        if array[i] == element:
            flag = len(array)
            helper = 0
            for j in range(flag-1, i, -1):
                if array[j] == element:
                    helper += 1
            array[flag - helper - 1], array[i] = element, array[flag - helper - 1]
    return array


def move_element_to_end_using_while(array, element):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == element:
            j -= 1
        if array[i] == element:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


array1 = [2, 2, 1, 3, 4, 2, 2, 2]
print(move_element_to_end_using_while(array1,2))
print(move_element_to_end(array1, 2))
