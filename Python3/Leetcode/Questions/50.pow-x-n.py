#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        result = self.helper(x, abs(n))

        return result if n > 0 else 1 / result

    def helper(self, x, n) -> int:
        if n == 0: return 1
        if n == 1: return x

        res = self.helper(x, n // 2)
        res = res * res
        return x * res if n % 2 else res
# @lc code=end

