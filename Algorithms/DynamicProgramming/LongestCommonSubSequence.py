def lcs(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    dp = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def slcs(first_string, second_string):
    dp = lcs(first_string, second_string)
    m = len(dp)-1
    n = len(dp[0])-1
    stack=[]
    while m>0 and n>0:
        if dp[m][n]==dp[m-1][n]:
            m=m-1
        elif dp[m][n]==dp[m][n-1]:
            n=n-1
        else:
            stack.append(first_string[m-1])
            m=m-1
            n=n-1
    output=""
    while len(stack)>0:
        cur=stack.pop()
        output=output+cur
    return output



first_string = "axyb"
second_string = "abyxb"

print(lcs(first_string, second_string))
print(slcs(first_string,second_string))