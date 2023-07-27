class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length() < s1.length()) return false;
        
        int[] s1arr = new int[26];
        int[] s2arr = new int[26];
        
        for(int i = 0; i < s1.length(); i++){
            s1arr[s1.charAt(i) - 'a']++;
            s2arr[s2.charAt(i) - 'a']++;
        }
        
        int matches = 0;
        
        for(int i = 0; i < 26; i++){
            if(s1arr[i] == s2arr[i]) matches++;
        }
        
        int left = 0;
        
        for(int right = s1.length(); right < s2.length(); right++){
            if(matches == 26) return true;
            
            int index = s2.charAt(right) - 'a';
            s2arr[index]++;
            
            if(s1arr[index] == s2arr[index]) matches++;
            else if ((s1arr[index] + 1) == s2arr[index]) matches--;
            
            
            int lindex = s2.charAt(left) - 'a';
            s2arr[lindex]--;
            
            if(s1arr[lindex] == s2arr[lindex]) matches++;
            else if ((s1arr[lindex] - 1) == s2arr[lindex]) matches--;
            left++;
        }
        
        return matches == 26;
    }
}