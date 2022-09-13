from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
        print(max(dp), dp)
        return max(dp)