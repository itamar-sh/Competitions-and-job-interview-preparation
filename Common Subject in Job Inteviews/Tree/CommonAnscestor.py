class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given Binary Tree, find the lowest cmmon anscestor of p and q.
        Recursion Solution - need to see iterative solution
        """
        if root is None or root == p or root == q:
            return root

        # Find p/q in left subtree
        l = self.lowestCommonAncestor1(root.left, p, q)

        # Find p/q in right subtree
        r = self.lowestCommonAncestor1(root.right, p, q)

        # If p and q found in left and right subtree of this node, then this node is LCA
        if l and r:
            return root

        # Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return l if l else r