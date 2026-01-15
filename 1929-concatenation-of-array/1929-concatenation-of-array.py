class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [n for i in range(2) for n in nums]