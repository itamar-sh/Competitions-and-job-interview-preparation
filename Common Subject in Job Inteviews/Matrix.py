from typing import List


class Matrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        state = 0
        state_dict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        seen = set()
        res = []
        i, j = 0, -1
        while i < len(matrix) and j < len(matrix[0]):
            next_i = i + state_dict[state][0]
            next_j = j + state_dict[state][1]
            print("res", res, "i", i, "next_i", next_i, "j", j, "next_j", next_j)
            if next_i < 0 or next_i >= len(matrix) or next_j < 0 or next_j >= len(matrix[0]) or next_i * len(
                    matrix[0]) + next_j in seen:
                state = (state + 1) % 4
            i += state_dict[state][0]
            j += state_dict[state][1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or i * len(matrix[0]) + j in seen:
                return res
            seen.add(i * len(matrix[0]) + j)
            res.append(matrix[i][j])

    def testSpiralOrder(self):
        assert(self.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5])

