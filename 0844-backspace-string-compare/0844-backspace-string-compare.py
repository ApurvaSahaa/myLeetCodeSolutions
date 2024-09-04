class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sstack = []
        for c in s:
            if c == '#' and sstack:
                sstack.pop()
            elif c != '#':
                sstack.append(c)
        tstack = []
        for c in t:
            if c == '#' and tstack:
                tstack.pop()
            elif c != '#':
                tstack.append(c)
                
        return sstack == tstack