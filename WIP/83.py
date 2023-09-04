# Helpful imports
# List
from typing import List, Optional  # Import the List type hint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        comparator = head.val
        locomotive = head
        caboose = head

        # Starting at second to utilize comparator
        if locomotive.next:
            print("if locomotive, L = C.next")
            locomotive = caboose.next
        

        else:
            return head
        print(f"[C L]")
        while locomotive:
            comparator = caboose.val
            print(f"[{caboose.val} {locomotive.val}]")

            while locomotive.val == comparator:
                if locomotive.next:
                    locomotive = locomotive.next
                    caboose.next = locomotive
                    
                else:
                    caboose.next = None
                    break

            print(locomotive.val)
            caboose = locomotive
            locomotive = locomotive.next
        self.printLinkedList(head)   

    def printLinkedList(self, head: Optional[ListNode]):
        current = head
        print()
        while current:
            print(f"Current val {current.val} -> ")
            current = current.next
        print("None")

def main():
    # Create a linked list: 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 5 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    
    solution = Solution()
    print("Original Linked List:")
    solution.printLinkedList(head)

    new_head = solution.deleteDuplicates(head)
    print("\nLinked List after deleting duplicates:")
    solution.printLinkedList(new_head)

if __name__ == "__main__":
    main()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        comparator = head.val