class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        maxval = arr[-1]
        arr[-1] = -1
        
        for i in range(len(arr) - 2, -1, -1):
            curr = arr[i]
            arr[i] = maxval
            if curr > maxval:
                maxval = curr
        return arr
        '''
        p = -1
        g = arr[-1]
        while p >= -len(arr):
            t = arr[p]
            arr[p] = g
            if t > g:
                g = t
            p -= 1
        arr[-1] = -1
        return arr