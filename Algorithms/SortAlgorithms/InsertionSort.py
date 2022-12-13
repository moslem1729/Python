def insertion_sort(number):
    for i in range(1, len(number)):
        current_number_index = i
        for j in range(i - 1, -1, -1):
            if number[current_number_index] < number[j]:
                number[current_number_index], number[j] = number[j], number[current_number_index]
                current_number_index = current_number_index - 1
            else:
                break
    return number


def insertion_sort_using_while(numbers):
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j = j - 1
    return numbers


numbers = [-90, 159, -4, -1, 9, 3, 69, 2, -1, 42, 8, 12, -87, 155, 200, -200]
print(insertion_sort_using_while(numbers))
numbers = [-90, 159, -4, -1, 9, 3, 69, 2, -1, 42, 8, 12, -87, 155, 200, -200]
print(insertion_sort(numbers))
