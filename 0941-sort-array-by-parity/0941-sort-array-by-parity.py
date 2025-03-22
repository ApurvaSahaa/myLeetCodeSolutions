class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        evenindex = 0
        evenchecker = 0
        
        while evenindex <= evenchecker and evenchecker < len(nums):
            if nums[evenchecker] % 2 == 0:
                nums[evenindex], nums[evenchecker] = nums[evenchecker], nums[evenindex]
                evenindex += 1
            evenchecker += 1
                
        return nums        