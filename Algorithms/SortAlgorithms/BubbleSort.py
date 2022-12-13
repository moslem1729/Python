def bubble_sort(numbers):
    for i in range(1, len(numbers)):
        check_if_swap_happen = 0
        for j in range(0, len(numbers) - i):
            if numbers[j] > numbers[j + 1]:
                swap(j,numbers)
                check_if_swap_happen = check_if_swap_happen + 1
        if check_if_swap_happen == 0:
            break
    return numbers


def bubble_sort_using_while(numbers):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(numbers) - 1 - counter):
            if numbers[i] > numbers[i + 1]:
                swap(i, numbers)
                is_sorted=False
        counter+=1
    return numbers


def swap(index, numbers):
    numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]


numbers = [159,-4,-1, 9, 3, 69, 2, -1, 42, 8, 12,-87,155]
print(bubble_sort_using_while(numbers))
print(bubble_sort(numbers))
