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
        '''
        if n < 0: 
            return False
        
        for i in range(31):
            number = 3 ** i
            if number == n:
                return True
            elif number > n:
                return False
        '''
        
        # n = 3 ^ i
        # i = log3(n)
        # i = log10(n) / log10(3)
        
        # logb(x) = loga(x)/loga(b)
        
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0