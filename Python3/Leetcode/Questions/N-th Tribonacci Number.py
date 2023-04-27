# Dynamic Programming - Memoization Approach - Time Complexity: O(n), Space Complexity: O(n) + O(n)
class Memoization:
    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.tribonacci_helper(n, memo)

    def tribonacci_helper(self, n: int, memo: {}):
        if n in memo: return memo[n]
        if n == 0: return 0
        if n <= 2: return 1

        memo[n] = self.tribonacci_helper(n - 1, memo) + self.tribonacci_helper(n - 2, memo) + self.tribonacci_helper(n - 3, memo)

        return memo[n]

# Dynamic Programming - Tabulation - Time Complexity: O(n), Space Complexity: O(n)
class Tabulation:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]