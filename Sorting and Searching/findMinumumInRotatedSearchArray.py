from typing import List


class Solution:
    def findBreak(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[(mid + 1) % len(nums)] < nums[mid]:
                return mid
            if nums[mid] < nums[0]:
                high = mid - 1
            elif nums[0] < nums[mid]:
                low = mid + 1
            else:
                return high
        return low

    def findMin(self, nums: List[int]) -> int:
        return nums[(self.findBreak(nums) + 1) % len(nums)]