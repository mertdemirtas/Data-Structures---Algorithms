#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    stack = []
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in mp:
                if stack and stack[-1] == mp[ch]:
                    stack.pop()
                else: return False
            else:
                stack.append(ch)

        return stack == []
# @lc code=end

