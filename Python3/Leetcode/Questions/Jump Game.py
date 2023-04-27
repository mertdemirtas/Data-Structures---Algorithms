from typing import List

# Dynamic Programming - Memoization Approach - Time Complexity: O(n*n), Space Complexity: O(n) + O(n)
class Memoization:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
          return True
        memo = {}
        return self.helper(nums, 0, memo)

    def helper(self, nums: List[int], index: int, memo: {}) -> bool:
        if index in memo: return memo[index]
        if index == len(nums) - 1: return True
        if index >= len(nums): return False
        if nums[index] == 0: return False

        memo[index] = False

        for jump in range(nums[index], 0, -1):
            if self.helper(nums, index + jump, memo):
              memo[index] = True
              return memo[index]
        return memo[index]

# Greedy Approach - Time Complexity: O(n), Space Complexity: O(1)
class Greedy:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
