class Solution {
    public int search(int[] nums, int target) {
        
        // pseudocode
        // we have a rotated sorted array with us and need to find a target
        // [3, 4, 5, 1, 2]
        // to implement a O(log(n)) complexity we need to implement some sort of binary search
        // initialize two pointers
            // left to 0
            // right to nums.length - 1
        // find middle element using left + (right  - left)/2
        // check if the middle value is equal to the target value, return if yes
        // now we can have two conditions
        // if we are in the left sorted array
            // if target > middle value or if target is smaller than left value 
                // we search to the right with left now becoming middle + 1
            // else the target is smaller than middle value or greater than left value
                // we search the left side with right becoming middle - 1
        // if we are in the right sorted array meaning middle value < left value
            // if target is smaller than middle value or the target is greater than the right value
            // we search the left of the array with right = middle - 1
            // else if the target is greater than the middle value and lesser than the right value we search
            // on the right side with left  = middle + 1
        
        // source code
        
        int left  = 0;
        int right = nums.length - 1;
        
        while (left <= right)
        {
            int middle  = left + (right - left)/2;
            
            if (target == nums[middle])
            {
                return middle;
            }
            
            if (nums[middle] >= nums[left])
            {
                if (target > nums[middle] || target < nums[left])
                {
                    left = middle + 1;
                }
                else
                {
                    right = middle - 1;
                }
            }
            else 
            {
                if (target < nums[middle] || target > nums[right])
                {
                    right = middle - 1;
                }
                else 
                {
                    left = middle + 1;
                }
            }
        }
        
        return -1;
        
    }
}