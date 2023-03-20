class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp_list = [0]*(n+1)
        dp_list[0] = 0
        dp_list[1] = 1

        i = 2
        ans = 1
        while i < n:
            # print(i)
            # print(i+1)
            prev_ind = i // 2
            dp_list[i] = dp_list[prev_ind]
            dp_list[i+1] = dp_list[prev_ind] + dp_list[prev_ind + 1]
            ans = max(ans, dp_list[i+1])
            i += 2
        # print(dp_list)
        return ans


if __name__ == "__main__":
    input_list = [
        15,
    ]
    sol = Solution()
    for input_data in input_list:
        n = input_data
        print(sol.getMaximumGenerated(n=n))
