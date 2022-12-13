from operator import le


def four_number_sum(array,target):
    all_pair_sums={}
    quadruplets=[]
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            current_sum=array[i]+array[j]
            diffrence=target-current_sum
            if diffrence in all_pair_sums:
                for pair in all_pair_sums[diffrence]:
                    quadruplets.append(pair+[array[i],array[j]])
            for k in range(i):
                current_sum=array[i]+array[k]
                if current_sum not in all_pair_sums:
                    all_pair_sums[current_sum]=[[array[k],array[i]]]
                else:
                    all_pair_sums[current_sum].append([array[k],array[i]])
    return quadruplets


array = [7, 6, 4, -1, 1, 2]
print(four_number_sum(array, 16))



