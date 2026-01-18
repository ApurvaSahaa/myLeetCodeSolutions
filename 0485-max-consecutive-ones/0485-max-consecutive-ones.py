class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pointer = consecutive_ones = 0
        while pointer <= len(nums) - 1:
            temp_ones = 0
            while pointer <= len(nums) - 1 and nums[pointer] == 1:
                temp_ones += 1
                pointer += 1
            if temp_ones >= consecutive_ones:
                consecutive_ones = temp_ones
            pointer += 1
        return consecutive_ones