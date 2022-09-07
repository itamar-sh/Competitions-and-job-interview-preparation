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
            # print("res", res, "i", i, "next_i", next_i, "j", j, "next_j", next_j)
            if next_i < 0 or next_i >= len(matrix) or next_j < 0 or next_j >= len(matrix[0]) or next_i * len(
                    matrix[0]) + next_j in seen:
                state = (state + 1) % 4
            i += state_dict[state][0]
            j += state_dict[state][1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or i * len(matrix[0]) + j in seen:
                return res
            seen.add(i * len(matrix[0]) + j)
            res.append(matrix[i][j])

    def spiralOrder_short_solution(self, matrix: List[List[int]]) -> List[int]:
        if (len(matrix) == 0):
            return []

        new_matrix = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            new_lst = []
            for i in range(1, len(matrix), 1):
                new_lst.append(matrix[i][j])
            new_matrix.append(new_lst)

        return matrix[0] + self.spiralOrder(new_matrix)

    def spiralOrder_zip_solution(self, matrix: List[List[int]]) -> List[int]:
        zip_value = [zip(*matrix)]
        zip_value_rev = [zip(*matrix)][::-1]
        res = matrix and [*matrix.pop(0)] + self.spiralOrder_zip_solution([*zip(*matrix)][::-1])
        return res

    def testSpiralOrder(self):
        assert(self.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5])
        assert(self.spiralOrder_zip_solution([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5])
        assert(self.spiralOrder_short_solution([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5])


if __name__ == '__main__':
    m = Matrix()
    m.testSpiralOrder()

