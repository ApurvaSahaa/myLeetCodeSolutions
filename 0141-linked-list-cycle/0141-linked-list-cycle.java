/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        // pseudocode
        // we will use a fast and slow pointer here
        // initialise fast and slow pointers to head
        // fast pointer will move 2 steps while slow moves one step
        // if there is a cycle there will be no null at the end and the fast and slow will eventually meet
        // we return true if the fast == slow at any point
        // if there is no cycle then the while loop to check is the two pointers are null will exit
        // and we return false
        
        ListNode fast = head;
        ListNode slow = head;
        
        while (fast != null && fast.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow)
            {
                return true;
            }
        }
        
        return false;
        
    }
}