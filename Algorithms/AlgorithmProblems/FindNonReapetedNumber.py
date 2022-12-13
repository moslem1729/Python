# O(n) space(n)
def find_non_reapeted_number(numbers):
    dic={}
    for item in numbers:
        if str(item) in dic:
            del dic[str(item)]
        else:
            dic[str(item)]=1
    return dic.keys()


def find_non_reapeted_number_XOR(numbers):
    non_repeated_number=numbers[0]
    for i in range(1,len(numbers)):
        non_repeated_number=non_repeated_number^numbers[i]
    return non_repeated_number


numbers=[2,3,2,5,3,5,8,8,9]
print(find_non_reapeted_number(numbers))
print(find_non_reapeted_number_XOR(numbers))