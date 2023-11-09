# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            if l1:
                num1 += str(l1.val)
                l1 = l1.next

        while l2:
            if l2:
                num2 += str(l2.val)
                l2 = l2.next

        num1 = num1[::-1]
        num2 = num2[::-1]
        
        num1 = int(num1)
        num2 = int(num2)

        num1 += num2
    
        num1 = str(num1)
        num1 = num1[::-1]
        print(num1)
        head = ListNode(0)
        result = head
        
        for i in range(0, len(num1)):
            new_node = ListNode(num1[i])
            head.next = new_node
            head = head.next

        result = result.next
        return result
        
def Main():
    s = Solution()
    test_1 = [3, 5, 7]
    test_2 = [2, 5, 4]
    answer = s.addTwoNumbers(test_1, test_2)
    print(answer)
    
Main()