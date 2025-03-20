class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count >= ans:
                    ans = count
                count = 0
        return max(ans, count)