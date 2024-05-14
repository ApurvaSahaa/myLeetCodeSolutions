class Solution {
    public boolean isPalindrome(String s) {
        
        // pseudocode
        // initialize two pointers
            // one at the start of the string (left)
            // other at the end of the string (right)
        // check if left pointer is smaller than the right pointer
        // check if the character at either the left or right pointer is anything other than a character
            // if character at left pointer is false then move left pointer forward by 1 and repeat step
            // similar to previous step but move right pointer back by 1 and repeat step
        // (the previous two steps can be combined into a single while loop)
        // check if both characters are the same
            // if not same return false
        // (wrap the previous 4 steps in a for loop)
        // return true
        
        // source code
        for (int left = 0, right = s.length() - 1; left < right; left++, right--)
        {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;
            
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) return false;
        }
        
        return true;
    }
}
