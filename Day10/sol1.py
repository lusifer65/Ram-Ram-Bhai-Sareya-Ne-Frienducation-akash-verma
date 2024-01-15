def findPages(arr: [int], n: int, m: int) -> int:

    def helper(arr, n, m, curr_max):
        students_required = 1
        current_sum = 0

        for i in range(n):
            if arr[i] > curr_max:
                return False

            if current_sum + arr[i] > curr_max:
                students_required += 1
                current_sum = arr[i]

                if students_required > m:
                    return False
            else:
                current_sum += arr[i]

        return True


    if n < m:
        return -1

    total_pages = sum(arr)
    start, end = max(arr), total_pages
    result = float('inf')

    while start <= end:
        mid = (start + end) // 2
        if helper(arr, n, m, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result if result != float('inf') else -1