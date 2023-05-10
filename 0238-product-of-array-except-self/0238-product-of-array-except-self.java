class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;

        int[] ans = new int[length];
        
        int prefix = 1;
        int postfix = 1;
        
        // we will now write the forward pass for the prefix array
        for(int i = 0; i < length; i++){
            ans[i] = prefix;
            prefix *= nums[i];
        }
        
        // array becomes ans ---> [1, 1, 2, 6]
        
        // now we will write the backward pass for the postfix array
        for(int i = length - 1; i >= 0; i--){
            ans[i] *= postfix;
            postfix *= nums[i];
        }
        
        // array becomes ans ---> [24, 12, 8, 6]
        
        return ans;
    }
}