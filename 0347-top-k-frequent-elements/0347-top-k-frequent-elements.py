class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #edge case since there is always a unique solution here
        if len(nums) == k:
            return nums
        #create the hashmap for elements and their frequencies
        nmap = {}
        for i in nums:
            nmap[i] = nmap.get(i, 0) + 1
        #building the max heap for k number of elements
        return heapq.nlargest(k, nmap.keys(), key=nmap.get)