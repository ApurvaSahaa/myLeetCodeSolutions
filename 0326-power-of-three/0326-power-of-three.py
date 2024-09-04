class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        number = n
        while number > 0:
            if number == 1:
                return True
            number /= 3
        return False
        
        '''
        
        if n < 0: 
            return False
        
        for i in range(31):
            number = 3 ** i
            if number == n:
                return True
            elif number > n:
                return False
            