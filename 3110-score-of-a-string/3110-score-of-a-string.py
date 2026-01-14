class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        while l < r and r < len(s):
            temp = abs(ord(s[r]) - ord(s[l]))
            res += temp
            l += 1
            r += 1
        return res