class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        #prefix and postfix method 
        prefix, postfix = [0]*len(nums), [0]*len(nums)
        l, r = 1, len(nums) - 2
        prefix[0] = 1
        postfix[-1] = 1
        #[1,2,3,4]
        
        while l < len(nums) and r >= 0:
                prefix[l] = nums[l - 1] * prefix[l-1]
                postfix[r] = nums[r + 1] * postfix[r + 1]
                l += 1
                r -= 1
        return [prefix[i] * postfix[i] for i in range(len(nums))]