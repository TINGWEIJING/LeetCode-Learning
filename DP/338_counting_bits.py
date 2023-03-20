from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]
        if n < 2:
            return ans[:n+1]

        offset = 2
        for i in range(2, n+1):
            refInd = i - offset
            if refInd >= offset:
                offset *= 2
                refInd = i - offset
            ans.append(1 + ans[refInd])
            # print(i)

        return ans


if __name__ == "__main__":
    input_list = [
        0,
        1,
        2,
        5
    ]
    sol = Solution()
    for input_data in input_list:
        n = input_data
        print(sol.countBits(n=n))
