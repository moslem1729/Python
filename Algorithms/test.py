
numbers=[1,8,9,6,4,2]
x=4


def sortkardan(numbers):
    for i in range(len(numbers)-1):
        min_value_index=i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[min_value_index]:
                min_value_index=j
        numbers[i],numbers[min_value_index]=numbers[min_value_index],numbers[i]
    return numbers

x=sortkardan([1,8,9,6,4,2])


mahgol_income=[100,200,300]
moslem_income=[1000,2000,3000]

mahgol_income=[100,200,300]
moslem_income=[1000,2000,3000]

def mean(listt):
    return((sum(listt)/len(listt)))




mahgol_income={100,200,300}
moslem_income={200,300,100}
if {300,100}.issubset(mahgol_income):
    print("yes")



