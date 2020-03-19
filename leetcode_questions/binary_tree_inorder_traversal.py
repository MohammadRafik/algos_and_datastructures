# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recursion(self, root: TreeNode):
        if root.left != None:
            yield from self.recursion(root.left)
        yield root.val
        if root.right != None:
            yield from self.recursion(root.right)


    def inorderTraversal(self, root: TreeNode):
        sol = []
        try:
            for value in self.recursion(root):
                sol.append(value)
            return sol
        except:
            return []
            


node = TreeNode(44)
node.right = TreeNode(22)
node.left = TreeNode(55)
node.left.right = TreeNode(420)

x = Solution()
print(x.inorderTraversal(node))
