class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # finding middle element(middle to last)
        fast = head
        slow = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        # print("middle",slow)
  
        # reverse the linked list upto (middle element to last)
        prev = None  
        current = slow
        while (current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        # print("reverse:",prev)

        # checking both linkedlists (first to middle) to (middle to last)
        fast = head
        slow = prev
        while slow != None:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
