class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        sub = ''
        for c in s:
            if c not in sub:
                sub += c
                ans = max(ans, len(sub))
            else:
                cut = sub.index(c)
                sub = sub[cut + 1:] + c
        return ans