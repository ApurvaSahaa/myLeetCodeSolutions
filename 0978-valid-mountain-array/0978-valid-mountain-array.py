class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        l, r = 1, len(arr) - 2
        
        while l <= r:
            if l == r and arr[l] > arr[l - 1] and arr[r] > arr[r + 1]:
                return True
            
            if r - l == 1 and arr[l] != arr[r] and arr[l] > arr[l - 1] and arr[r] > arr[r + 1]:
                return True
            
            if arr[l] > arr[l - 1] and arr[r] > arr[r + 1]:
                l += 1
                r -= 1
            else:
                return False
        
        return False