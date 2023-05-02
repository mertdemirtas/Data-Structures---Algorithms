#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        
        window = nums[0]

        for r in range(1, len(nums)):
            window += nums[r]
            if nums[r] > window:
                window = nums[r]
            res = max(res, window)
        return res

# @lc code=end

