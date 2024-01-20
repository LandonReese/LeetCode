# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        head = current

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                current = list2
                list2 = list2.next
            else:
                current.next = list1
                current = list1
                list1 = list1.next

        if list1 or list2:
            current.next = list1 if list1 else list2

        return head.next


def main():
    inputs = [

    ]

    outputs = [

    ]

    s = Solution()

    for i in range(0, len(inputs)):
        a,b = inputs[i]
        assert(s.mergeTwoLists(a,b) == outputs[i])

if __name__ == "__main__":
    main()