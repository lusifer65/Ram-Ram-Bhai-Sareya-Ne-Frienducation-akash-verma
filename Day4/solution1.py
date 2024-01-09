class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxSum=-1e8
        curr=0

        for i in range(n):
            curr+=nums[i]
            if(maxSum<curr):
                maxSum=curr
            if(curr<0):
                curr=0
        return maxSum