class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxAr = Integer.MIN_VALUE;
        while(left < right){
            maxAr = Integer.max(maxAr, ((right - left) * Integer.min(height[left], height[right])));
            if(height[left] <= height[right]) left++;
            else right--;
        }
        return maxAr;
    }
}