class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # given array of integers
        # one original integer --> first number that needs to be searched for in array
        # if original is found multiply original by 2
        # otherwise stop the process --> break out
        # repeat the process with new number as long as you keep finding the number
        # return final value of original
        
        in_there = True
        
        while in_there:
            if original in nums:
                original = original * 2
            else:
                in_there = False
        
        return original
        