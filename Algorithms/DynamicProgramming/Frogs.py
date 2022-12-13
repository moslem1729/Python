import copy


def frogs(stones):
    dp=[0,abs(stones[1]-stones[0])]
    dp_with_value={(0):[stones[0]],(1):[stones[0],stones[1]]}
    for i in range(2,len(stones)):
        dp_with_value[(i)]=[]
        first_way=dp[i-2]+abs(stones[i]-stones[i-2])
        second_way=dp[i-1]+abs(stones[i]-stones[i-1])
        if first_way<second_way:
            dp.append(first_way)
            temp=copy.copy(dp_with_value[(i-2)])
            temp.append(stones[i])
            dp_with_value[(i)]=temp
        else:
            dp.append(second_way)
            temp=copy.copy(dp_with_value[(i-1)])
            temp.append(stones[i])
            dp_with_value[(i)]=temp
    return dp_with_value


def frogs_k(stones,k):
    dp=[0]
    dp_with_value = {(0): [stones[0]]}
    for i in range(1,len(stones)):
        if i<=k:
            current_smallest_cost=dp[0]+abs(stones[i]-stones[0])
            current_index=0
            for j in range(1,i):
                if dp[j]+abs(stones[i]-stones[j])<=current_smallest_cost:
                    current_smallest_cost=dp[j]+abs(stones[i]-stones[j])
                    current_index=j
            dp.append(current_smallest_cost)
            temp=copy.copy(dp_with_value[(current_index)])
            temp.append(stones[i])
            dp_with_value[(i)]=temp
        else:
            current_smallest_cost=dp[i-k]+abs(stones[i]-stones[i-k])
            current_index=i-k
            for j in range(i-k+1,i):
                if dp[j]+abs(stones[i]-stones[j])<=current_smallest_cost:
                    current_smallest_cost=dp[j]+abs(stones[i]-stones[j])
                    current_index=j
                dp.append(current_smallest_cost)
                temp = copy.copy(dp_with_value[(current_index)])
                temp.append(stones[i])
                dp_with_value[(i)] = temp
    return dp_with_value



stones=[30,20,40,50,100,-10,20,90,40,-30]

print(frogs(stones))
print(frogs_k(stones,3))
