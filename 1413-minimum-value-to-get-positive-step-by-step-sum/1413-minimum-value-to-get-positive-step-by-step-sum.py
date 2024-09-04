class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # the total should never be less than 1
        '''
        if nums[0] < 0:
            res = -nums[0] + 1
        else:
            res = 1
        
        # need to set res to be at least 1
        # start iterating from next index
        # if total ever drops less than 1
        # run a loop incrementing res and total till total becomes 1
        # finally return res
        
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
        
        '''
        
        total = 0
        res = 1
        for i in nums:
            total += i
            res = max(res, 1 - total)
        return res