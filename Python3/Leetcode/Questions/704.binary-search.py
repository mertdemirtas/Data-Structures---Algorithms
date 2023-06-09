#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = int(l + (r - l) / 2)

            if nums[mid] == target: return mid
            if nums[mid] < target: l = mid + 1
            if nums[mid] > target: r = mid - 1
        
        return -1
# @lc code=end

