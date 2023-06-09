# MARK: Dynamic Programming
from typing import List

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