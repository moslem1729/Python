def next_greater_element(numbers):
    result = []
    for i in range(len(numbers)):
        start_index = i + 1
        end_index = i
        while True:
            if start_index == end_index:
                result.append(-1)
                break
            if start_index == len(numbers):
                start_index = 0
            else:
                if numbers[start_index] > numbers[i]:
                    result.append(numbers[start_index])
                    break
                else:
                    start_index += 1
    return result


def next_greater_element_stack(nums):
    result = [-1 for _ in nums]
    stack = []
    for idx in range(2 * len(nums)):
        circular_index = idx % len(nums)
        while len(stack) > 0 and nums[stack[len(stack) - 1]] < nums[circular_index]:
            top = stack.pop()
            result[top] = nums[circular_index]
        stack.append(circular_index)
    return result


numbers = [2, 5, -3, -4, 6, 7, 2]
print(next_greater_element(numbers))
print(next_greater_element_stack(numbers))
