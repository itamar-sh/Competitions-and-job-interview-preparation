from idlelib.tree import TreeNode
from typing import Optional, List
from collections import namedtuple, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class OrderTraversal:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        there is better way, called: Morris Traversal - with O(1) extra space.
        this solution have O(n) extra space because it's get inside recursion O(n) times and this takes O(n) new args.
        :param root: head
        :return: values in nodes
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        traversal by level but the even level from left to right and odd right to left.
        :param root: head
        :return: values in nodes
        """
        if not root:
            return []
        res = []
        level = -1
        queue = deque()
        Node = namedtuple("Node", ["TreeNode", "level"])
        queue.append(Node(root, 0))
        rightOrder = True
        while queue:
            # decide side
            if queue[0].level == queue[-1].level and queue[0].level != level:
                level += 1
                rightOrder = not rightOrder
                res.append([])
            # pop item
            if rightOrder:
                value = queue.pop().TreeNode  # from right to left
            else:
                value = queue.popleft().TreeNode  # from left to right
            # print value
            res[level].append(value.val)
            # insert items
            if rightOrder:
                if value.right:
                    queue.appendleft(Node(value.right, level + 1))  # from right to left
                if value.left:
                    queue.appendleft(Node(value.left, level + 1))  # from right to left
            else:
                if value.left:
                    queue.append(Node(value.left, level + 1))  # from right to left
                if value.right:
                    queue.append(Node(value.right, level + 1))  # from right to left
        return res

    def connectWhenFullBunaryTree(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        -Populating Next Right Pointers in Each Node - Medium - 116-
        connect each node to his right in the tree. so node.next will bring you to your neighbor.
        full binary tree.
        :param root:
        :return:
        """
        if not root:
            return
        current = root
        if current.left:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
            self.connectWhenFullBunaryTree(current.left)
            self.connectWhenFullBunaryTree(current.right)
        return root

    def findNextChild(self, current: 'Node'):
        """
        helper for connectWithoutFullBinaryTree.
        find next node in order.
        :param current:
        :return:
        """
        if current.left:
            return current.left
        elif current.right:
            return current.right
        elif current.next:
            return self.findNextChild(current.next)
        else:
            return None

    def connectWithoutFullBinaryTree(self, root: 'Node') -> 'Node':
        """
        -Populating Next Right Pointers in Each Node - Medium - 116-
        connect each node to his right in the tree. so node.next will bring you to your neighbor.
        NOT full binary tree.
        :param root:
        :return:
        """
        if not root:
            return
        current = root
        # connect next to each child
        if current.left:
            if current.right:
                current.left.next = current.right
            elif current.next:
                current.left.next = self.findNextChild(current.next)
            else:
                current.left.next = None
        if current.right:
            if current.next:
                current.right.next = self.findNextChild(current.next)
            else:
                current.right.next = None
        # keep connect down the levels
        self.connectWithoutFullBinaryTree(current.right)
        self.connectWithoutFullBinaryTree(current.left)
        return root
