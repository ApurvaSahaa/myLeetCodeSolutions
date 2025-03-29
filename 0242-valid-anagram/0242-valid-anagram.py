class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ca = [0]*26
        for i in range(len(s)):
            ca[ord(s[i]) - ord('a')] += 1
            ca[ord(t[i]) - ord('a')] -= 1
        
        for i in ca:
            if i != 0:
                return False
        return True