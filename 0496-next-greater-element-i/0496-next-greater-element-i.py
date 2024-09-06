class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        
        mapping = {}
        res = []
        stack = []
        stack.append(nums2[0])
        
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        while stack:
            mapping[stack.pop()] = -1
        
        for i in range(len(nums1)):
            res.append(mapping[nums1[i]])
        
        return res