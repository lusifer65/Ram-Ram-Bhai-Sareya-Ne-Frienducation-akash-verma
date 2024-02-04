from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]

    max_sum = [0] * n
    max_sum[0] = max(0, nums[0])
    max_sum[1] = max(max_sum[0], nums[1])

    for i in range(2, n):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + nums[i])

    return max_sum[-1]

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1