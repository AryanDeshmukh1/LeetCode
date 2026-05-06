/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node to handle edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;

        // Traverse while at least two nodes exist
        while (prev.next != null && prev.next.next != null) {

            // Nodes to swap
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Swapping
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // Move prev to next pair
            prev = first;
        }

        return dummy.next;
    }
}