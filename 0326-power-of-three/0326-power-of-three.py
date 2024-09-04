class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        number = n
        while number > 0:
            if number == 1:
                return True
            number /= 3
        return False