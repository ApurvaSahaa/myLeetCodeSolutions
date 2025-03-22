class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastnonzerofoundat = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastnonzerofoundat] = nums[i]
                lastnonzerofoundat += 1
        for i in range(lastnonzerofoundat, len(nums)):
            nums[i] = 0
        