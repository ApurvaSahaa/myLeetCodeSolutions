class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            int b = target - nums[i];
            if(map.containsKey(b)){
                int[] ans = {i, map.get(b)};
                return ans;
            }
            else map.put(nums[i], i);
        }
        return new int[2];
    }
}