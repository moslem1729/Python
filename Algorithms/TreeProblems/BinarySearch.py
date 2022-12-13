def binary_search_recursive(array, number, low, high):
    if low > high:
        return False
    else:
        mid = (high - low) // 2
        if array[mid] == number:
            return mid
        elif array[mid] < number:
            return binary_search_recursive(array, number, mid + 1, high)
        else:
            return binary_search_recursive(array, number, low, mid - 1)


def binary_search_iterative(array, number):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == number:
            return mid
        elif array[mid] < number:
            low = mid + 1
            continue
        else:
            high = mid - 1
            continue
    return False


arr = [1, 2, 4, 9, 12, 16, 19]
print(binary_search_iterative(arr, 1))
print(binary_search_recursive(arr, 1, 0, len(arr) -1))
