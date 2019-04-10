# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        r = False
        l = False
        if root is None:
            return False
        if root.right:
            r = r or self.hasPathSum(root.right,sum-root.val)
        if root.left:
            l = l or self.hasPathSum(root.left,sum-root.val)
        if (sum-root.val == 0 and not root.right and not root.left) or r or l :
            return True
        else:
            return False
        
        