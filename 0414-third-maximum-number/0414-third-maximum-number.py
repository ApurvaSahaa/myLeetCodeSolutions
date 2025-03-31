class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        
        if len(s) > 2:
            for i in range(2):
                s.remove(max(s))
        
        return max(s)