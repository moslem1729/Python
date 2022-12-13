def selection_sort(numbers):
    for i in range(len(numbers)-1):
        min_value_index=i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[min_value_index]:
                min_value_index=j
        numbers[i],numbers[min_value_index]=numbers[min_value_index],numbers[i]

    return numbers


numbers=[99,-13,1,2,9,4,6,5,-12,86,-15]
print(selection_sort(numbers))


