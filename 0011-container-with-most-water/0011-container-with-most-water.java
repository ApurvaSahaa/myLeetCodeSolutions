class Solution {
    public int maxArea(int[] height) {
        
        // pseudocode
        // we are given an unsorted integer array with numbers representing varying water levels
        // we can use two pointers
        // volume of water = (right pointer - left pointer) * minimum of number at (left pointer , right pointer)
        // initialize pointers
            // left pointer at the left extreme of array
            // right pointer at the right extreme of array
        // initialize a integer variable to contain the maximum volume till current loop
        // check if left pointer < right pointer before entering a loop
        // check the temporary volume and compare with max volume 
            // if max volume < temp volume, assign temp volume to max volume
            // if max volume >= temp volume, move ahead
        // check and compare heights at left and right pointer
            // if height at left pointer <= height at right pointer, left++
            // else right--
        // return max volume
        
        
        //source code
        
        int left = 0;
        int right = height.length - 1;
        int maxVolume = Integer.MIN_VALUE;
        
        while (left < right)
        {
            int tempVolume  = (right - left) * Integer.min(height[left], height[right]);
            maxVolume  = Integer.max(maxVolume, tempVolume);
            if (height[left] <= height[right]) left++;
            else right--;
        }
        
        return maxVolume;
        
    }
}