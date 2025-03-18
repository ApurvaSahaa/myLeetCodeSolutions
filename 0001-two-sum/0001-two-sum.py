class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nmap = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nmap.keys():
                return [i, nmap[rem]]
            nmap[nums[i]] = i
        return []