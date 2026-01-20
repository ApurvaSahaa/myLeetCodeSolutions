class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapdict = {}
        s = len(nums)
        if s == 1:
            return nums[0]
        for n in nums:
            if n in mapdict.keys():
                mapdict[n] = mapdict.get(n) + 1
                if mapdict.get(n) > s/2:
                    return n
            else:
                mapdict[n] = 1