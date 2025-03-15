class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
           
        HashSet<Integer> numSet = new HashSet<>();
        for(int i: nums){
            numSet.add(i);
        } 

        int longest = 1;

        for(int i: numSet){
            if(!numSet.contains(i - 1)){
                int currNum = i;
                int currLen = 1;
                while(numSet.contains(currNum + 1)){
                    currNum++;
                    currLen++;
                }
                longest = Math.max(longest, currLen);
            }
        }

        return longest;

    }
}