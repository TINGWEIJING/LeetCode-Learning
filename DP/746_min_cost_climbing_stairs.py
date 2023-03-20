from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]

        dp_list = [0]*len(cost)
        dp_list[-2:] = cost[-2:]
        # print(dp_list)
        for i in range(len(cost) - 3, -1, -1):
            dp_list[i] = cost[i] + min(dp_list[i+1], dp_list[i+2])
        # print(dp_list)
        return min(dp_list[0], dp_list[1])


if __name__ == "__main__":
    input_list = [
        [10, 15],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ]
    sol = Solution()
    for input_data in input_list:
        cost = input_data
        print(sol.minCostClimbingStairs(cost=cost))
