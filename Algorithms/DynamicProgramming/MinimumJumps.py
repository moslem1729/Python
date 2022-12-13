from pandas import array


def minimum_jumps(numbers):
    length=len(numbers)-1

    
    start_index=0
    next_index=0
    result=str(numbers[start_index])+" -->"
    while True:
        best_jump=0
        for i in range(start_index+1,start_index+numbers[start_index]+1):
            if numbers[i]+i>best_jump:
                best_jump=i
        next_index=best_jump
        result=result+str(numbers[next_index])+"-->"
        if next_index+numbers[next_index]>=length:
            result=result+str(numbers[length])
            break
        start_index=next_index
    return result

numbers=[3,4,2,1,2,3,7,1,1,1,2,5]
print(minimum_jumps(numbers))
            