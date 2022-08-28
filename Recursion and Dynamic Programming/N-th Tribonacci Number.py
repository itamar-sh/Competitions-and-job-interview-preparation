class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1, 2]
        for i in range(4, n+1):
            nums.append(nums[i-1]+nums[i-2]+nums[i-3])
        return nums[n]

    def tribonacci_no_space(self, n: int) -> int:
        nums = [0, 1, 1, 2]
        for i in range(4, n+1):
            nums[i % 4] = nums[i-1 % 4]+nums[i-2 % 4]+nums[i-3 % 4]
        return nums[n]