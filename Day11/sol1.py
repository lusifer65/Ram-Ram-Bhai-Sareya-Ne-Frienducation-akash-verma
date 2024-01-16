def findLargestMinDistance(board:list, k:int):

    def total(arr, frm, to):
        total = 0
        for i in range(frm, to + 1):
            total += arr[i]
        return total

    def helper(arr, n, k, memo):
        if k == 1:
            return total(arr, 0, n - 1)
        if n == 1:
            return arr[0]

        if (n, k) in memo:
            return memo[(n, k)]

        best = float('inf')

        for i in range(1, n + 1):
            best = min(best, max(helper(arr, i, k - 1, memo), total(arr, i, n - 1)))

        memo[(n, k)] = best
        return best


    memo = {}
    return helper(board, len(board), k, memo)

