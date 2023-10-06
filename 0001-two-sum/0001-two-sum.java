class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        // a + b = target
        // so we get a, and need to see if b is present in the hashmap
        // b = target - a
        // we store a as the key and the index as value
        
        for (int i = 0; i < nums.length; i++)
        {
            // a is nums[i] and we need to find b
            int b = target - nums[i];
            if (map.containsKey(b))
            {
                int[] ans = {i, map.get(b)};
                return ans;
            }
            else
            {
                map.put(nums[i], i);
            }
        }
        return new int[2];
    }
}