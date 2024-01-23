class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash={};
        for i in range(0,len(nums)):
            hash[nums[i]]=(hash[nums[i]]+1) if(nums[i] in hash) else 1
        # print(hash)
        for i in nums:
            if(hash[i]==1):
                return i

        return -1