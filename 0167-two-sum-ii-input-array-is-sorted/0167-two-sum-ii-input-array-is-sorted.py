class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            tempsum = numbers[l] + numbers[r]
            if tempsum > target:
                r -= 1
            elif tempsum < target:
                l += 1
            else:
                return [l + 1, r + 1]