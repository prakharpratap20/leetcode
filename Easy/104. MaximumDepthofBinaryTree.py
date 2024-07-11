"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Definition for a binary tree node.
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
