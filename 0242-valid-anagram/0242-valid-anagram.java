class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        
        int[] temp = new int[26];
        
        for(char c : s.toCharArray()){
            temp[c - 'a']++;
        }
        for(char c : t.toCharArray()){
            temp[c - 'a']--;
        }
        
        for(int i : temp){
            if(i != 0) return false;
        }
        
        return true;
    }
}