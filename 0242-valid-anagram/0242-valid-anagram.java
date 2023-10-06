class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] tmp = new int[26];
        
        for (char c: s.toCharArray())
        {
            tmp[c - 'a']++;
        }
        
        for (char c: t.toCharArray())
        {
            tmp[c - 'a']--;
        }
        
        for (int i = 0; i < tmp.length; i++)
        {
            if (tmp[i] != 0) return false;
        }
        
        return true;
    }
}