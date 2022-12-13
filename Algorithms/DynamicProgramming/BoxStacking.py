import copy
   
   

def box_stacking(boxes):
    sorted_boxes = sort_boxes(boxes)
    dp = [0 for _ in boxes]
    dp_with_value = {(0): []}
    for i in range(len(boxes)):
        dp_with_value[(i)]=[]
        for j in range(i):
            if dp[i] < dp[j] and sorted_boxes[j][1] <= sorted_boxes[i][1] and sorted_boxes[j][2] <= sorted_boxes[i][2]:
                dp[i] = dp[j]
                dp_with_value[(i)] = copy.copy(dp_with_value[(j)])
        dp[i] += 1
        temp=copy.copy(dp_with_value[(i)])
        temp.append(sorted_boxes[i])
        dp_with_value[i] = temp
    return dp_with_value


def sort_boxes(boxes):
    result = []
    for i in range(len(boxes)):
        current_smallest = boxes[i]
        for j in range(i, len(boxes)):
            if boxes[j][0] < current_smallest[0]:
                current_smallest = boxes[j]
        result.append(current_smallest)
    return result


boxes = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
print(box_stacking(boxes))
