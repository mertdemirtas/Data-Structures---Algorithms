#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26

        for ch in magazine:
            arr[ord(ch) - 97] += 1
        
        for ch in ransomNote:
            ch_index = ord(ch) - 97
            if arr[ch_index] > 0: arr[ch_index] -= 1
            else: return False
        
        return True
        
        


# @lc code=end

