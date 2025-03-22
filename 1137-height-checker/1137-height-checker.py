class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h != sh for h, sh in zip(heights, sorted(heights)))