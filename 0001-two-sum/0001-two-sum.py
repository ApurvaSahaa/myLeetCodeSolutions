class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nmap.keys():
                return [nmap[diff], i]
            else:
                nmap[nums[i]] = i