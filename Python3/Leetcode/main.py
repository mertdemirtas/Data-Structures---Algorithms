# MARK: Dynamic Programming
from typing import List

class NthTribonacciNumber:
    def __init__(self):
        n = 25
        print(self.__tribonacci(n))

    def __tribonacci(self, n: int) -> int:
        return self.__tribonacci_helper(n)

    def __tribonacci_helper(self, n: int, memo = {}):
        if n in memo: return memo[n]
        if n == 0: return 0
        if n <= 2: return 1

        memo[n] = self.__tribonacci_helper(n - 1) + self.__tribonacci_helper(n - 2) + self.__tribonacci_helper(n - 3)

        return memo[n]

    def run(self, n: int):
        self.__tribonacci(n)

class MinCostClimbingStairs:

    def __init__(self):
        arr = [1,100,1,1,1,100,1,1,100,1]
        print("Min cost to reach the top of stairs:", self.__min_cost_climbing_stairs(arr))

    def __min_cost_climbing_stairs(self, cost: []) -> int:
        return min(self.__min_cost_climbing_stairs_helper(cost, len(cost) - 1), self.__min_cost_climbing_stairs_helper(cost, len(cost) - 2))

    def __min_cost_climbing_stairs_helper(self, cost: [], n, memo = {}):
        if n in memo: return memo[n]
        if n < 0: return 0

        memo[n] = cost[n] + min(self.__min_cost_climbing_stairs_helper(cost, n - 1, memo), self.__min_cost_climbing_stairs_helper(cost, n - 2, memo))
        return memo[n]

    def run(self, arr: []):
        print("Min cost to reach the top of stairs:", self.__min_cost_climbing_stairs(arr))

class HouseRobber:
    def __init__(self):
        arr = [2,7,9,3,1]
        print("Max profit for house robbing:", self.__rob(arr))

    def __rob(self, nums: []) -> int:
        return max(self.__rob_helper(nums, len(nums) - 1), self.__rob_helper(nums, len(nums) - 2))

    def __rob_helper(self, nums: [], n, memo = {}):
        if n in memo: return memo[n]
        if n < 0: return 0

        memo[n] = nums[n] + max(self.__rob_helper(nums, n - 2, memo), self.__rob_helper(nums, n - 3, memo))
        return memo[n]

    def run(self, arr: []):
        print("Max profit for house robbing:", self.__rob(arr))


nth_tribonacci_number = NthTribonacciNumber()
climbing_stairs = MinCostClimbingStairs()
house_robber = HouseRobber()

def rob(nums: List[int]) -> int:
    return max(robHelper(nums, len(nums) - 1), robHelper(nums, len(nums) - 2))


def robHelper(nums: List[int], n: int, memo={}) -> int:
    if n in memo: return memo[n]
    if n < 0: return 0

    memo[n] = nums[n] + max(robHelper(nums, n - 2, memo), robHelper(nums, n - 3, memo))
    print(memo)
    return memo[n]

arr = [1,2,10,200,233,30]
print(rob(arr))