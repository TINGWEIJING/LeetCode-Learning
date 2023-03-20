from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans_list = [[1]]
        if numRows == 1:
            return ans_list

        ans_list.append([1, 1])
        if numRows == 2:
            return ans_list

        for i in range(2, numRows):
            print(i)
            prev_pascal_row = ans_list[i-1]
            pascal_row = [1]
            for j in range(1, i):
                pascal_row.append(prev_pascal_row[j-1] + prev_pascal_row[j])

            pascal_row.append(1)
            ans_list.append(pascal_row)
        return ans_list


if __name__ == "__main__":
    input_list = [
        5,
    ]
    sol = Solution()
    for input_data in input_list:
        numRows = input_data
        print(sol.generate(numRows=numRows))
