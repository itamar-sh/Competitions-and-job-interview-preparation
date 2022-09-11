from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        # find pivot - O(log(n))
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while high != low:
            mid = (high + low) // 2
            if nums[mid] > nums[mid+1]:
                break
            if nums[mid] < nums[0]:
                high = mid - 1
            elif nums[mid] > nums[0]:
                low = mid + 1
            else:  # low + 1 = mid so high is the solution
                mid = high
                break
        # find target
        if target > nums[0]:
            high = mid
            low = 0
        elif nums[0] > target:
            low = mid+1
            high = len(nums) - 1
        else:  # target == nums[0]
            return 0
        mid = (high + low) // 2
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                break
        mid = (high + low) // 2
        return mid if nums[mid] == target else -1

solver = Solution()
print(solver.search([2,3,4,5,1], 1)) # 4
print(solver.search([2,3,4,1], 1)) # 3
print(solver.search([3,4,5,1,2], 1)) # 3
print(solver.search([3,4,5,1,2], 4)) # 1
print(solver.search([3,4,5,1,2], 6)) # -1
print(solver.search([6], 6)) # 0
print(solver.search([5], 6)) # -1
print(solver.search([7], 6)) # -1
print(solver.search([7,6], 6)) # 1
print(solver.search([7,8,6], 6)) # 2
print(solver.search([7,8,6], 7)) # 0
print(solver.search([8,6,7], 8)) # 0
print(solver.search([4,5,6,7,0,1,2], 0)) # 4
print(solver.search([4,5,6,7], 4)) # 0
print(solver.search([4,5,6,7], 3)) # -1
print(solver.search([4,5,6], 3)) # -1
print(solver.search([4,5], 3)) # -1
print(solver.search([1,3], 0)) # -1
