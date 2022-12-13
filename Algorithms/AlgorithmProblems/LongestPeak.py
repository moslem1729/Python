def longest_peak(array):
    longest__peak = 0
    current_peak = 1
    peaks = find_peaks(array)
    for index in peaks:
        current_number_index = index
        next_number_index = index + 1
        previous_number_index = index - 1
        while True:
            if array[previous_number_index] < array[current_number_index]:
                current_peak += 1
                current_number_index = previous_number_index
                previous_number_index -= 1
            else:
                break
        current_number_index = index
        while True:
            if array[next_number_index] < array[current_number_index]:
                current_peak += 1
                current_number_index = next_number_index
                next_number_index += 1
            else:
                break
        if longest__peak < current_peak:
            longest__peak = current_peak
        current_peak = 1
    return longest__peak


def find_peaks(array):
    peaks = []
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            peaks.append(i)
    return peaks


def longest_peak_better_solution(array):
    longest_peak_length = 0
    i = 1
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] > array[i + 1]
        if not is_peak:
            i = i + 1
            continue

        j = i - 2
        while j >= 0 and array[j] < array[j + 1]:
            j = j - 1
        k = i + 2
        while k < len(array) and array[k] < array[k - 1]:
            k = k + 1

        current_peak_length = k - j - 1

        longest_peak_length = current_peak_length if current_peak_length > longest_peak_length else longest_peak_length

        i = k + 1

    return longest_peak_length


arr = [1, 2, 3, 3, 4, 0, 10, 11, 6, 5, -1, -3, 2, 3]
print(longest_peak_better_solution(arr))
print(longest_peak(arr))
