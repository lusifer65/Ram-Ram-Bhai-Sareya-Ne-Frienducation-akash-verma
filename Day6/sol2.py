class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # nums.sort()
        h={}
        for i in nums:
            h[i]=h[i]+1 if(i in h) else 1
        
        ans=0

        for i,v in h.items():
            if(k>0 and i+k in h or k==0 and h[i]>1):
                ans+=1
        # print(nums)
        return ans