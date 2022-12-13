def three_largest_number(array):
    three_largest=[array[i] for i in range(3)]
    for i in range(2,len(array)):
        if array[i]>three_largest[2]:
            three_largest[0]=three_largest[1]
            three_largest[1]=three_largest[2]
            three_largest[2]=array[i]
        elif array[i]>three_largest[1]:
            three_largest[0]=three_largest[1]
            three_largest[1]=array[i]
        elif array[i]>three_largest[0]:
            three_largest[0]=array[i]
        else:
            continue

    return three_largest


numbers=[1,454,44,-45,89,35]
for item in three_largest_number(numbers):
    print(item)