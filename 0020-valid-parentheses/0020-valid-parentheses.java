class Solution {
    public boolean isValid(String s) {
        
        // pseudocode
        // we have a string that we will treal like a list of characters
        // we will use the stack data structure
        
        // we loop over the string characters
            // if any of the characters are one of the opening type we push its corresponding closing type into a stack
            // else we check the character with the stack.pop and if they are equal we move on or we return false
            // we just return the boolean value of stack.isEmpty()
        
        // source code
        
        Stack<Character> stack = new Stack<>();
        
        if (s.length() == 0 || s.length() == 1)
        {
            return false;
        }
        
        for (int i = 0; i < s.length(); i++)
        {
            if (s.charAt(i) == '(')
            {
                stack.push(')');
            }
            else if (s.charAt(i) == '{')
            {
                stack.push('}');
            }
            else if (s.charAt(i) == '[')
            {
                stack.push(']');
            }
            else if (stack.isEmpty() || s.charAt(i) != stack.pop())
            {
                return false;
            }
        }
        
        return stack.isEmpty();
    }
}