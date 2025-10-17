class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy= ListNode(0)
        head=dummy
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            summ = x + y + carry
            digit = summ % 10
            carry = summ // 10

            head.next = ListNode(digit)
            head = head.next 
            
            if l1:
                l1=l1.next
            
            if l2:
                l2=l2.next
        return dummy.next
