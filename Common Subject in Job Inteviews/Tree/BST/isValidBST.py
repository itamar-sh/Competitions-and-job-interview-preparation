import sys
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    """
    def _isValidBST_helper(self, root: Optional[TreeNode], min_val: int, max_val: int) -> Tuple[bool, int, int]:
        if not root:
            return True
        # check if it's valid from the roots:
        if root.val <= min_val or root.val >= max_val:
            return False
        # check if the left right nodes are ok
        if (root.left and root.val <= root.left.val) or (root.right and root.val >= root.right.val):
            return False
        return self._isValidBST_helper(root.left, min_val, min(max_val, root.val)) and \
               self._isValidBST_helper(root.right, max(min_val, root.val), max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST_helper(root, -1 - sys.maxsize, sys.maxsize)