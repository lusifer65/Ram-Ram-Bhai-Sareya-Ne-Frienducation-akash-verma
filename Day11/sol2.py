class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if(i>0 and i not in h):
                h[i]=1
        
        for i in range(len(h)):
            if(i+1 not in h):
                return i+1
        return len(h)+1