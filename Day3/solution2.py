class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_dict = {0: 1}
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sum_dict:
                count += sum_dict[current_sum - k]
            sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1

        return count