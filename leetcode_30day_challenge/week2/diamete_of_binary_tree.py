# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        list_of_depths = []


        def recursion(Node, list = [0, 0]):
            if Node.left:
                recursion(Node.left)
            
            if Node.right:
                recursion(Node.right)


        def recursion__(Node):


x = TreeNode(5)
TreeNode.left = 420
TreeNoe.right = 69