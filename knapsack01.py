N = 5 # Number of items
weights = [2, 4, 1, 4, 3]
values = [3, 2, 1, 5, 2]
Wcapacity = 9

dp = [[0 for i in range(Wcapacity + 1)] for j in range(N + 1)]
ans = 0

for i in range(1, N + 1):
    wt = weights[i - 1]
    for w in range(0, Wcapacity + 1):
        if(w - wt < 0):
            dp[i][w] = dp[i - 1][w]
            continue
        dp[i][w] = max(dp[i - 1][w - wt] + values[i - 1], dp[i - 1][w])
        ans = max(ans, dp[i][w])

print(ans)