import math
from typing import List
from pprint import pprint

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # edge case: if only 1 point
        if len(points) < 2:
            return 1

        rad__connection_set = {}

        for i in range(len(points)):
            pt_1 = points[i]
            for j in range(i+1, len(points)):
                pt_2 = points[j]

                dy = pt_1[1] - pt_2[1]
                dx = pt_1[0] - pt_2[0]

                if dx > 0 or dx < 0:
                    angle_rad = math.atan(dy/dx)
                    intersection_c = pt_1[1] - (dy/dx) * pt_1[0]
                else:
                    angle_rad = math.radians(90)
                    intersection_c = pt_1[0]

                rad_key = angle_rad

                rad__connection_set.setdefault((rad_key, intersection_c), set([tuple(pt_1)]))
                rad__connection_set[(rad_key, intersection_c)].add(tuple(pt_2))

        # edge case: not found
        if len(rad__connection_set) < 1:
            return 0

        max_count = 0
        for rad_key, pt_set in rad__connection_set.items():
            total_count = len(pt_set)
            if total_count > max_count:
                max_count = total_count

        return max_count


if __name__ == "__main__":
    input_list = [
        # [[1, 1], [2, 2], [3, 3]],
        # [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
        # [[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]],
        # [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
        [[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]],
    ]
    sol = Solution()
    for input_data in input_list:
        print(sol.maxPoints(input_data))
