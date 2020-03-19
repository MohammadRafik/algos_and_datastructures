# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sol_list = []
    def inorderTraversal(self, root: TreeNode):
        
        if root.left != None:
            self.inorderTraversal(root.left)
        self.sol_list.append(root.val)
        if root.right != None:
            self.inorderTraversal(root.right)


node = TreeNode(44)
node.right = TreeNode(22)
node.left = TreeNode(55)
node.left.right = TreeNode(420)

x = Solution()
x.inorderTraversal(node)
print(x.sol_list)