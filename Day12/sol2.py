class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h={}
        n=len(nums)
        for i in nums:
            h[i]=h[i]+1 if(i in h) else 1
        
        for i in nums:
            if(h[i]>n//2):
                return i
        
        return -1