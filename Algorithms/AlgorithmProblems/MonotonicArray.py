def monotonic_array(array):
    flag = []
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            flag.append(1)
        if array[i] < array[i + 1]:
            flag.append(-1)
    if len(flag) == 0:
        return True

    first_flag = flag[0]
    for item in flag:
        if first_flag != item:
            return False
    return True


def monotonic_array_another_solution(array):
    flag = 0
    current_idx = 0
    last_idx = len(array) - 1
    while current_idx < last_idx:
        if array[current_idx] < array[current_idx + 1]:
            if flag == -1:
                return False
            else:
                flag = 1
                current_idx += 1
        elif array[current_idx] > array[current_idx + 1]:
            if flag == 1:
                return False
            else:
                flag = -1
                current_idx += 1
        else:
            current_idx += 1
    return True


def is_monotonic(array):
    is_non_decreasing = True
    is_non_increasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False
    return is_non_increasing or is_non_decreasing


array = [2, 1, 1, 2, 3, 11, 11, 122]
print(is_monotonic(array))
print(monotonic_array(array))
print(monotonic_array_another_solution(array))
