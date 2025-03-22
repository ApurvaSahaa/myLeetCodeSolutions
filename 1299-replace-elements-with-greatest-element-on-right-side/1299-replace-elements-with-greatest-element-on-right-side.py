class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        maxright = -1
        for i in range(l - 1, -1, -1):
            curr = arr[i]
            arr[i] = maxright
            maxright = max(maxright, curr)
        return arr