from typing import List

# Dynamic Programming - Memoization Approach - Time Complexity: O(n), Space Complexity: O(n) + O(n)
class Memoization:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.helper(cost, len(cost) - 1, memo), self.helper(cost, len(cost) - 2, memo))

    def helper(self, cost: List[int], n, memo: {}):
        if n in memo: return memo[n]
        if n < 0: return 0

        memo[n] = cost[n] + min(self.helper(cost, n - 1, memo), self.helper(cost, n - 2, memo))
        return memo[n]