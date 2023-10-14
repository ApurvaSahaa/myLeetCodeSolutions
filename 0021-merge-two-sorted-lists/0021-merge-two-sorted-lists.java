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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        // pseudocode
        // we start with a head node pointing to null
        // we compare the values of the start pointers of the two lists
        // we set the next pointer for the head node to the node with smaller value
        // we then keep comparing the values till the list.next values are pointing to null
        // once both the lists are null we return head.next
        
        
        // source code
        
        ListNode root = new ListNode();
        
        ListNode head = root;
        
        while (list1 != null && list2 != null)
        {
            if (list1.val <= list2.val)
            {
                head.next = list1;
                list1 = list1.next;
            }
            else
            {
                head.next = list2;
                list2 = list2.next;
            }
            head = head.next;
        }
        head.next = list1 != null ? list1 : list2;
        
        return root.next;
    }
}