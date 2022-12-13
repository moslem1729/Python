def spiral_traverse(array):
    result=[]
    start_row,end_row=0,len(array)-1
    start_column,end_column=0,len(array[0])-1
    while start_row<=end_row and start_column<=end_column:
        for column in range(start_column,end_column+1):
            result.append(array[start_row][column])

        for row in range(start_row+1,end_row+1):
            result.append(array[row][end_column])

        for column in reversed(range(start_column,end_column)):
            result.append(array[end_row][column])

        for row in reversed(range(start_row+1,end_row)):
            result.append(array[row][start_column])

        start_row+=1
        end_row-=1
        start_column+=1
        end_column-=1

    return result


arr=[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
print(spiral_traverse(arr))

