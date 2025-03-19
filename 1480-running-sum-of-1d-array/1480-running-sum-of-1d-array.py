class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            ans[i] = val
        return ans