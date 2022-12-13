def minimum_waiting_time_2for(array):
    sum = 0
    array.sort()
    array_helper = []
    for i in array[:-1]:
        array_helper.append(i)
        for j in array_helper:
            sum = sum + j

    return sum


def minimum_waiting_time(queries):
    queries.sort()
    total_waiting_time = 0
    for index, value in enumerate(queries):
        queries_left = len(queries) - (index + 1)
        total_waiting_time = total_waiting_time + value * queries_left
    return total_waiting_time


time_list = [3,2,1,2,6]
print(minimum_waiting_time(time_list))
print(minimum_waiting_time_2for(time_list))
