def vacation(activities):
    dp = [[0 for _ in activities[0]] for _ in activities]
    dp[0]=activities[0]
    number_of_days = len(activities)
    number_of_activities = len(activities[0])
    for i in range(1, number_of_days):
        for j in range(number_of_activities):
            max_happiness = 0
            for k in range(number_of_activities):
                if k != j:
                    if dp[i - 1][k] > max_happiness:
                        max_happiness = dp[i - 1][k]
            dp[i][j] = activities[i][j] + max_happiness
    return dp


activities = [[10, 70, 90], [20, 50, 80], [30, 60, 70]]
print(vacation(activities))