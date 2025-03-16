class Solution:
    def trap(self, height: List[int]) -> int:
        #initialize total array same len as height and all 0s
        #get the l and r pointers
        #as we move through the height array
        #take left till the end and right till the beginning
        #while doing that keep replacing the total array with min values

        total = [10**5 + 1]*len(height)
        l, r = 0, len(height) - 1
        maxlh= height[l]
        maxrh = height[r]
        while l < len(height) and r >= 0:
            maxlh = max(maxlh, height[l])
            maxrh = max(maxrh, height[r])
            leftwater = maxlh - height[l]
            rightwater = maxrh - height[r]
            total[l] = min(total[l], leftwater)
            total[r] = min(total[r], rightwater)
            l += 1
            r -= 1
        return sum(total)