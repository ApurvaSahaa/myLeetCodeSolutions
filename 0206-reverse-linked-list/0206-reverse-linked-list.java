/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        // pseudocode
        // we just need to change the direction for the pointers
        // we see that a node has next and previous
        // declare 3 pointers 
            // one previous pointer pointing to NULL
            // one current pointer pointing to the node being modified
            // one next pointer pointing to NULL
        // while current pointer is not NULL
        // first temporarily change the next pointer to current.next
        // change current.next to previous
        // change previous to current
        // change current to next
        // stop the loop when current pointer points to NULL and return previous
        
        // source code
        
        ListNode prev = null;
        ListNode current = head;
        ListNode nextCurrent = null;
        
        while (current != null)
        {
            nextCurrent = current.next;
            current.next = prev;
            prev = current;
            current = nextCurrent;
        }
        
        return prev;
        
    }
}