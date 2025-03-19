class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        wmap = {}
        for i in ransomNote:
            wmap[i] = wmap.get(i, 0) + 1
        for i in magazine:
            if i in wmap.keys():
                wmap[i] -= 1
        for v in wmap.values():
            if v > 0:
                return False
        return True
