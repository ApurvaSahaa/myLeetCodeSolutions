class Solution {
    public int findMin(int[] nums) {
        
        // pseudo code
        // rotated array - [3, 4, 5, 1, 2] 
        // to run using O(log(n)) we will need to use some sort of binary search
        // maintain a variable with the smallest value, initialize it arbritarily to the value at index 0
        // initialize the two starting pointers
            // left to 0
            // right to array.length - 1
        // get into a while loop till the condition left <= right is met
        // check if the number at the left pointer is less than the number at the right pointer
        // return the value at the left pointer since this means that the array is in its initial sorted form
        
        // otherwise calculate the middle value using left + (right - left)/2
        // replace the variable with smallest value between current middle value and existing value
        // check if we are in the left sorted array or right sorted array
        // if the middle value is greater than the left value then we know that we are in the left sorted array
        // and need to continue our search on the right sorted array or right side
        
        // else if the middle value is smaller than the left value we are in the right sorted array and need to
        // continue our search on the left side
        // return the variable with the smallest value in the end
        
        // source code
        
        int left = 0;
        int right  = nums.length - 1;
        
        int minValue = nums[0];
        
        while (left <= right)
        {
            if (nums[left] < nums[right])
            {
                return Integer.min(minValue, nums[left]);
            }
            
            int middle = left + (right - left)/2;
            
            minValue = Integer.min(minValue, nums[middle]);
            
            if (nums[middle] >= nums[left])
            {
                left = middle + 1;
            }
            else 
            {
                right = middle - 1;
            }
        }
        
        return minValue;
    }
}

