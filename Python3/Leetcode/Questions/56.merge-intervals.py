#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals

        intervals.sort(key=lambda x: x[0])

        arr = []
        temp = intervals[0]
        print(temp)
        for element in range(1, len(intervals)):
            if temp[1] >= intervals[element][0]:
                temp[1] = max(temp[1], intervals[element][1])
            else:
                arr.append(temp)
                temp = [intervals[element][0], intervals[element][1]]
        
        if temp: arr.append(temp)

        return arr
# @lc code=end

