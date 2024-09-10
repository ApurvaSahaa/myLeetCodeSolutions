class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        '''
        # not possible since we use separate memory for stack
        stack = []
        for i in s:
            stack.append(i)
        while stack:
            for i in range(0, len(s)):
                s[i] = stack.pop()
        '''