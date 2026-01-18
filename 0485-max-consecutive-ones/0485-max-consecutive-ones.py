class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = temp_ones = 0
        for num in nums:
            if num == 1:
                temp_ones += 1
            else:
                if temp_ones >= ones:
                    ones = temp_ones
                temp_ones = 0
        return max(ones, temp_ones)