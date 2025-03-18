class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        ans = [1]*len(nums)
        l = 1
        r = len(nums) - 2
        lp = 1
        rp = 1
        while l < len(nums) and r >= 0:
            lp = nums[l - 1]*lp
            rp = nums[r + 1]*rp
            ans[l] = lp*ans[l]
            ans[r] = rp*ans[r]
            l += 1
            r -= 1
            
        return ans
        