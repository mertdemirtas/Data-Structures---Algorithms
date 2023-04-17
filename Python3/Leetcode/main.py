# MARK: Dynamic Programming
class MinCostClimbingStairs:
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
    def __rob(self, nums: []) -> int:
        return max(self.__rob_helper(nums, len(nums) - 1), self.__rob_helper(nums, len(nums) - 2))

    def __rob_helper(self, nums: [], n, memo = {}):
        if n in memo: return memo[n]
        if n < 0: return 0

        memo[n] = nums[n] + max(self.__rob_helper(nums, n - 2, memo), self.__rob_helper(nums, n - 3, memo))
        return memo[n]

    def run(self, arr: []):
        print("Max profit for house robbing:", self.__rob(nums))

climbing_stairs = MinCostClimbingStairs()
cost = [1,100,1,1,1,100,1,1,100,1]
climbing_stairs.run(cost)

house_robber = HouseRobber()
nums = [2,7,9,3,1]
house_robber.run(nums)

# ---------------------------------------------------------------------------------

