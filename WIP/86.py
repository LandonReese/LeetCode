# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        maxValue = -101
        for ListNode in Optional:
            if ListNode < x:
                if ListNode.val > maxValue:
                    maxValue = ListNode.val
                    print(maxValue)

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
                        
# Create a sample linked list
nodes = [ListNode(1), ListNode(4), ListNode(3), ListNode(2), ListNode(5), ListNode(2)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

# Test the partition function
solution = Solution()
x = 3
partitioned_head = solution.partition(head, x)
print("Partitioned linked list:")
print_linked_list(partitioned_head)