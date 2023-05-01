#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        arr_2 = [0] * 26
        for ch in s:
            arr[ord(ch) - 97] += 1
        
        for ch in t:
            arr_2[ord(ch) - 97] += 1

        return arr == arr_2
# @lc code=end

