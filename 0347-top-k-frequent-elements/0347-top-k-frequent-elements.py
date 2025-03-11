class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        nmap = {}
        for i in nums:
            nmap[i] = nmap.get(i, 0) + 1
        
        return heapq.nlargest(k, nmap.keys(), key=nmap.get)