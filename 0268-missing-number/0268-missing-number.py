class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n * (n+1))//2
        
        sum_of_arr = 0
        for i in nums:
            sum_of_arr += i
            
        return total_sum - sum_of_arr