class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # the total should never be less than 1
        
        if nums[0] < 0:
            res = -nums[0] + 1
        else:
            res = 1
        
        index = 1
        total = res + nums[0]
        while index < len(nums):
            total += nums[index]
            if total < 1:
                while total < 1:
                    res += 1
                    total += 1
            index += 1
        return res
            