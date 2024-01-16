def findLargestMinDistance(board:list, k:int):

    def sum(board, frm, to):
        total = 0
        for i in range(frm, to + 1):
            total += board[i]
        return total

    n=len(board)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + board[i - 1]

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = prefix_sum[i]

    for i in range(1, k + 1):
        dp[1][i] = board[0]

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            for p in range(1, i):
                dp[i][j] = min(dp[i][j], max(dp[p][j - 1], prefix_sum[i] - prefix_sum[p]))

    return dp[n][k]
