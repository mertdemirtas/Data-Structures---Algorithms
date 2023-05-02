#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_arr = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in set_arr:
                set_arr.remove(s[l])
                l += 1
            set_arr.add(s[r])
            res = max(res, r - l + 1)

        return res
# @lc code=end

