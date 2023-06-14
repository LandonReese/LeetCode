# NOT FINISHED RESUME LATER

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Return variable for the smallest difference between two nodes in the tree
        # Initialized at the next largest integer larger than the possible node value
        self.minDifference = 100001
        # print(self.minDifference)

        # Dictionary for each value in tree
        valueList = []

        # Initialized at -2 to differentiate nodes.
        self.previousNodeVal = -2

        # Traverse the tree recursively to check all nodes
        def inOrder(TreeNode):
        
            # Base Case
            if TreeNode is None:
                return

            # Recursive Case
            self.getMinimumDifference(TreeNode.left)
            #print("TreeVal", TreeNode.val)
            valueList.append(TreeNode.val)
            # print("PrevNodeVal", self.previousNodeVal)
            #if TreeNode.val


            self.getMinimumDifference(TreeNode.right)

        inOrder(root)

        print("Gate 1")
        for val1 in valueList:
            print("Gate 2")
            for val2 in valueList:
                print("Gate 3")
                if(val1 != val2):
                    numDifference = abs(val1 - val2)
                    print("numDifference", numDifference)
                    if numDifference < self.minDifference:
                        self.minDifference = numDifference

        # Return the minimum absolute difference
        return self.minDifference

        # 1. Traverse the left subtree, i.e., call Inorder(left->subtree)
        # 2. Visit the root.
        # 3. Traverse the right subtree, i.e., call Inorder(right->subtree)