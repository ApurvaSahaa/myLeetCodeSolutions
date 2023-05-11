class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        Set<Integer> set = new HashSet<>();
        int ans = 1;
        for(int i: nums) set.add(i);
        for(int i: nums){
            if(!set.contains(i - 1)){
                int count = 1;
                while(set.contains(i + 1)){
                    count++;
                    i++;
                }
                ans = Math.max(ans, count);
            }
        }
        
        return ans;
    }
}