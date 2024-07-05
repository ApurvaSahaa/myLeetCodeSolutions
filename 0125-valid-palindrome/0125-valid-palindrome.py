class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        
        for i in s:
            if i.isalpha() or i.isdigit():
                new += i.lower()
        
        return new == new[::-1]