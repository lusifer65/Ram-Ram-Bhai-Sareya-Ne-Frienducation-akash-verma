class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ind = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[ind]:
                ind += 1
                nums[ind] = nums[i]
        return ind + 1
