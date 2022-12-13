def merge_overlapping_intervals(array):
    array=sorted(array,key=lambda x:x[0])
    i = 0
    while i < len(array) - 1:
        if is_interval(array[i], array[i + 1]):
            array[i] = merge_intervals(array[i], array[i + 1])
            array.remove(array[i + 1])
        else:
            i += 1

    return array


def is_interval(first_array, second_array):
    if second_array[0] <= first_array[1]:
        return True
    else:
        return False


def merge_intervals(first_array, second_array):
    merge_array = [1 for _ in first_array]
    merge_array[0] = first_array[0]
    merge_array[1] = second_array[1]
    return merge_array


arr = [[3, 5], [4, 7], [7, 8], [9, 10],[1, 2]]
print(merge_overlapping_intervals(arr))
