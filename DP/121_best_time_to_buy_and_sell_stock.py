from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_list = [0]*len(prices)
        dp_list[-1] = prices[-1]
        output = 0
        for i in range(len(prices)-2, -1, -1):
            buy_price = prices[i]
            sell_price = dp_list[i+1]
            profit = sell_price - buy_price
            if profit > output:
                output = profit
            # update dp array
            dp_list[i] = max(buy_price, sell_price)
        # print(dp_list)
        return output


if __name__ == "__main__":
    input_list = [
        [7, 1],
        [1, 7],
        [7, 1, 7],
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
    ]
    sol = Solution()
    for input_data in input_list:
        prices = input_data
        print(sol.maxProfit(prices=prices))
