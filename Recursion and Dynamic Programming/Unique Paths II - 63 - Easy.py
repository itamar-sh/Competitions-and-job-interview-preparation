class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        resultGrid = [[0] * len(obstacleGrid[0]) for g in obstacleGrid]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    resultGrid[i][j] = 1 - obstacleGrid[0][0]
                elif obstacleGrid[i][j] == 1:
                    resultGrid[i][j] = 0
                elif i == 0:
                    resultGrid[i][j] = resultGrid[i][j - 1]
                elif j == 0:
                    resultGrid[i][j] = resultGrid[i - 1][j]
                else:
                    resultGrid[i][j] = resultGrid[i][j - 1] + resultGrid[i - 1][j]
        return resultGrid[-1][-1]