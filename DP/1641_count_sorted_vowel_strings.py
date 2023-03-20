class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp_list = [1, 1, 1, 1, 1]
        for i in range(n):
            new_dp_list = [1]*len(dp_list)
            accum = 0
            for k in range(len(dp_list)-1, -1, -1):
                accum += dp_list[k]
                new_dp_list[k] = accum
            # print(new_dp_list)
            dp_list = new_dp_list
        return dp_list[0]


if __name__ == "__main__":
    input_list = [
        # 1,
        # 2,
        # 33,
        55,
    ]
    sol = Solution()
    for input_data in input_list:
        n = input_data
        print(sol.countVowelStrings(n=n))
