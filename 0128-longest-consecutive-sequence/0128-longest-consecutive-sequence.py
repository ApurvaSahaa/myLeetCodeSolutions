class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the list into a set
        # iterate over it and check if the number is the start of a sequence
        # we do that by checking if the left neighbor exists in the set
        # if it does not then it is a start
        # then we start trying to check to the right of the number
        # once we reach the end and no more right neighbor exists we end the count
        numset = set(nums)
        if len(nums) == 0:
            return 0
        longest = 1
        for i in numset:
            if i - 1 not in numset:
                currNum = i
                currLen = 1
                while currNum + 1 in numset:
                    currNum += 1
                    currLen += 1
                longest = max(longest, currLen)
        return longest