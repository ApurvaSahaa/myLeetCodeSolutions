class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxleft = [0] * len(height)
        maxleft[0] = height[0]
        for i in range(1, len(height)):
            prevmax = maxleft[i-1]
            maxleft[i] = max(prevmax, height[i])
        
        maxright = [0] * len(height)
        maxright[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            prevmax = maxright[i + 1]
            maxright[i] = max(prevmax, height[i])
        
        water_trapped = [0] * len(height)
        for i in range(len(water_trapped)):
            water = (min(maxleft[i], maxright[i]) - height[i])
            if water > 0:
                water_trapped[i] = water
        res = 0
        for i in water_trapped:
            res += i
        
        return res