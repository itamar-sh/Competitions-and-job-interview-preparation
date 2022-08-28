# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __nextNodeGenerate(self, nums: List[int], start, end):
        if start == end:
            return None
        cur_len = end - start
        tree = TreeNode(nums[start + cur_len//2])
        if cur_len == 1:
            return tree
        tree.left = self.__nextNodeGenerate(nums, start, start + cur_len // 2)
        tree.right = self.__nextNodeGenerate(nums, start + cur_len // 2 + 1, end)
        return tree

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        tree = TreeNode(nums[len(nums) // 2])
        tree.left = self.__nextNodeGenerate(nums, 0, len(nums) // 2)
        tree.right = self.__nextNodeGenerate(nums, len(nums) // 2 + 1, len(nums))
        return tree

solver = Solution()
print(solver.sortedArrayToBST([0,1,2,3,4]))