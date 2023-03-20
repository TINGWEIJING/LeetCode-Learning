class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp_list = [0]*n
        dp_list[:2] = [1,2]
        for i in range(2, n):
            dp_list[i] = dp_list[i-1] + dp_list[i-2]
        return dp_list[-1]
    
if __name__ == "__main__":
    input_list = [
        2,
        3
    ]
    sol = Solution()
    for input_data in input_list:
        n = input_data
        print(sol.climbStairs(n=n))