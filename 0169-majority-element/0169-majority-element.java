class Solution {
    public int majorityElement(int[] nums) {
        
        Map<Integer, Integer> lookup = new HashMap<>();
        
        int max = Integer.MIN_VALUE;
        int ans = nums[0];
        
        for(int i = 0; i < nums.length; i++){
            lookup.put(nums[i], lookup.getOrDefault(nums[i], 0) + 1 );
            if (lookup.get(nums[i]) > max)
            {
                max = lookup.get(nums[i]);
                ans = nums[i];
            }
        }
        
        return ans;
    }
}