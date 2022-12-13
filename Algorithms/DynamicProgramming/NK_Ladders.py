

def nk_ladders(n,k):

    arr=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if i<=k:
            for j in range(i):
                arr[i]+=arr[j]
            arr[i]+=1
        else:
            for j in range(i-k,i):
                arr[i]+=arr[j]
    return arr[n]

print(nk_ladders(4,3))



