# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        def dfs(currRoot): #find the max height of tree, for both left and right sides
            if not currRoot:
                return 0
            left = dfs(currRoot.left)
            right = dfs(currRoot.right)
            self.res = max(self.res, left + right) # add both sides together to get the largest diameter
            return 1 + max(left,right)
        dfs(root)
        return self.res