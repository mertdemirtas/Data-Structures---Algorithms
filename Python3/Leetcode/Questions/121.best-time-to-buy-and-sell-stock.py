#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            temp = max(temp, prices[r] - prices[l])

        return temp
# @lc code=end

