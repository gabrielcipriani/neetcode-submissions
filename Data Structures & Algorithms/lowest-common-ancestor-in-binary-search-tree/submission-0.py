# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node is not None:
            if node.val > p.val and node.val > q.val: # must be left
                node = node.left
            elif node.val < p.val and node.val < q.val: # must be right
                node = node.right
            else: # either split, or this node is p or q
                return node