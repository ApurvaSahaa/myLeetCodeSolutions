class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int start = 0; int end = 0;
        Map<Character, Integer> map = new HashMap<>();
        while(end < s.length()){
            if(map.containsKey(s.charAt(end)) && map.get(s.charAt(end)) >= start){
                start = map.get(s.charAt(end)) + 1;
            }
               
            map.put(s.charAt(end), end);
               
            max = Math.max(max, end - start + 1);
            end++;
        }
    
        return max;
    }
}
