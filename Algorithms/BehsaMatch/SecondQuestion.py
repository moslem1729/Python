def knapsack(values,weights,knapsack_capacity):
    knapsack_values={}
    for j in range(knapsack_capacity+1):
        knapsack_values[(0,j)]=0
    
    for i in range(1,len(values)+1):
        for j in range(knapsack_capacity+1):
            if weights[i-1]<=j:
                knapsack_values[(i,j)]=max(knapsack_values[(i-1,j)],values[i-1]+knapsack_values[(i-1,j-weights[i-1])])
            else:
                knapsack_values[(i,j)]=knapsack_values[(i-1,j)]
            
    return knapsack_values[(len(values),knapsack_capacity)] ,get_knapsack_items(knapsack_values,values,weights,knapsack_capacity)
    

def get_knapsack_items(knapsack_values,values,weights,knapsack_capacity):
    sequence=[]
    i=len(values)
    j=knapsack_capacity
    while i>0:
        if knapsack_values[(i,j)]==knapsack_values[(i-1,j)]:
            i-=1
        else:
            sequence.append([values[i-1],weights[i-1],i-1])
            j-=weights[i-1]
            i-=1
        if j==0:
            break
    return list(reversed(sequence))
