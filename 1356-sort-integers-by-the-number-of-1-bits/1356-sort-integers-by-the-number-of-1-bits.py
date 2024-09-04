class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # given integer array
        
        return sorted(arr, key = lambda a: [bin(a).count('1'), a])