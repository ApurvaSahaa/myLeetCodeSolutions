# def findDigits(num: int) -> int:
#     digits = 0
#     while num != 0:
#         num = num // 10
#         digits += 1
#     return digits


class Solution: 
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            length = len(str(i))
            if length % 2 == 0:
                ans += 1
        return ans

    

            
    