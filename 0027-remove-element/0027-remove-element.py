class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = f = 0
        
        while s <= f and f < len(nums):
            if nums[f] == val:
                f += 1
            else:
                nums[s] = nums[f]
                f += 1
                s += 1
        return s
                