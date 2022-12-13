import copy
def longest_increasing_subsequence(numbers):
    dp=[0 for _ in numbers]
    dp_with_value={}
        
    for i in range(len(numbers)):
        dp_with_value[(i)]=[]
        j=i-1

        while j>0:
            if numbers[i]>numbers[j] and dp[i]<dp[j]:
                    dp[i]=dp[j]
                    dp_with_value[(i)]=dp_with_value[(j)]
            j-=1

        dp[i]+=1    
        temp=copy.copy(dp_with_value[(i)])
        temp.append(numbers[i])
        dp_with_value[(i)]=temp
    return dp_with_value


numbers=[50,4,10,8,30,100]
print(longest_increasing_subsequence(numbers))
