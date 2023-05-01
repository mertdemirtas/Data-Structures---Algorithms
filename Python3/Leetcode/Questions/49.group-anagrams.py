#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for ch in s:
                temp[ord(ch) - 97] += 1
        
            mp[tuple(temp)].append(s)

        return mp.values()

# @lc code=end

