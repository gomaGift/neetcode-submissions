# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        reverse = slow.next
        prev = slow.next = None


        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp

        
        curr = head
        while prev:
            curr_t = curr.next
            curr_p = prev.next
            curr.next = prev
            prev.next = curr_t
            curr = curr_t
            prev = curr_p
        


        
         

        


        