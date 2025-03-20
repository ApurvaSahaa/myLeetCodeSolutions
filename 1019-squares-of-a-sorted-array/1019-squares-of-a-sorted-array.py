class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [0]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
            ans[i] = square * square
        return ans