class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the list into a set
        # iterate over it and check if the number is the start of a sequence
        # we do that by checking if the left neighbor exists in the set
        # if it does not then it is a start
        # then we start trying to check to the right of the number
        # once we reach the end and no more right neighbor exists we end the count
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest