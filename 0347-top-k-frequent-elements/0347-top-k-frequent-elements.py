class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        for i in nums:
            if i in fmap.keys():
                fmap[i] += 1
            else:
                fmap[i] = 1
        
        l = [[k, v] for k, v in fmap.items()]
        l = sorted(l, key=lambda x:x[1], reverse=True)
        return [l[i][0] for i in range(k)]