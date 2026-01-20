class Solution:
    def maxDifference(self, s: str) -> int:
        mapdict = {}
        for c in s:
            if c in mapdict.keys():
                mapdict[c] = mapdict.get(c) + 1
            else:
                mapdict[c] = 1
        
        a1 = float("-inf")
        a2 = float("inf")
        for v in mapdict.values():
            if v % 2 == 1:
                if v > a1:
                    a1 = v
            else:
                if v < a2:
                    a2 = v
        return a1 - a2