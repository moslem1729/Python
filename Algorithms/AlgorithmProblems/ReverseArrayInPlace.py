def reverse_array(array):
    array_reversed = []
    for idx in range(len(array) - 1, -1, -1):
        array_reversed.append(array[idx])

    return array_reversed

def reversed_array(array):
    start=0
    end=len(array)-1
    while start<end:
        array[start],array[end]=array[end],array[start]
        start+=1
        end-=1
    return array



arr = [1, 2, 3, 4, 5]
arr1 = reverse_array(arr)
arr2=reversed_array(arr)
for element in arr2:
    print(element)


for element in arr1:
    print(element)
