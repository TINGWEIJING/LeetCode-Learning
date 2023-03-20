import math
from typing import List
from pprint import pprint


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # edge case: if only 1 point
        if len(points) < 2:
            return 1

        rad__connection_count = {}

        for i in range(len(points)):
            pt_1 = points[i]
            for j in range(i+1, len(points)):
                pt_2 = points[j]

                dy = pt_1[1] - pt_2[1]
                dx = pt_1[0] - pt_2[0]

                if dx > 0 or dx < 0:
                    angle_rad = math.atan(dy/dx)
                else:
                    angle_rad = math.radians(90)

                # rad_key = round(angle_rad, 6)
                rad_key = angle_rad

                rad__connection_count.setdefault(rad_key, 0)
                rad__connection_count[rad_key] += 1

        # edge case: not found
        if len(rad__connection_count) < 1:
            return 0

        pprint(rad__connection_count)

        max_count = max(rad__connection_count.values())

        # determine number of points
        count_2 = max_count * 2
        for i in range(len(points)):
            n = i+1
            n_1 = i
            if count_2 / (n) == n_1:
                return n

        return 0


if __name__ == "__main__":
    input_list = [
        # [[1,1],[2,2],[3,3]],
        # [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
        # [[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]],
        [[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]],
    ]
    sol = Solution()
    for input_data in input_list:
        print(sol.maxPoints(input_data))
