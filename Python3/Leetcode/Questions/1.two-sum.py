#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in mp:
                return [mp[temp], i]
            mp[nums[i]] = i
# @lc code=end

