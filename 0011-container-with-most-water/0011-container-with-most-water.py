class Solution:
    def maxArea(self, height: List[int]) -> int:
        #take two pointers
        #calculate the max water contained in them with the rectangle area
        #the height will be the minimum of the two heights
        #and the width will be the difference between indexes

        l, r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            localwater = h * w
            maxWater = max(maxWater, localwater)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return maxWater