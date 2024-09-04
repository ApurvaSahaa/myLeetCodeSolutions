class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # recursion --> TLE here
        if n == 0  or n == 1:
            return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        '''
        '''
        # memoization
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]):
        if n == 0 or n == 1:
            return 1
        
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
        
        '''
        
        # dynamic programming
        
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        
        
            
        