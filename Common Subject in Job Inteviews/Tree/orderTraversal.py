from idlelib.tree import TreeNode
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class OrderTraversal:
    # there is better way, called: Morris Traversal - with O(1) extra space.
    # this solution have O(n) extra space because it's get inside recursion O(n) times and this takes O(n) new args.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)