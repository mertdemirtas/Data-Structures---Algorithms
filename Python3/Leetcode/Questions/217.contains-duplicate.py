#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                return True
            mp[nums[i]] = 1
        
        return False

# @lc code=end

