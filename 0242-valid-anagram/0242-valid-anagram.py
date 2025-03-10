class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        stmap = [0]*26
        # s and t only contain lowercase english letters
        for i in s:
            stmap[ord(i) - ord('a')] += 1
        for i in t:
            stmap[ord(i) - ord('a')] -= 1
        for i in stmap:
            if i != 0:
                return False
        return True
