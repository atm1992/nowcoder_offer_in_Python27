# -*- coding: UTF-8 -*-
"""
机器人的运动范围。
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

解题思路：类似于上一题。
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        visited = [False] * (rows * cols)
        return self.movingCountCore(threshold, rows, cols, 0, 0, visited)

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if 0 <= row < rows and 0 <= col < cols and self.judgeCoord(threshold, row, col) and not visited[row * cols + col]:
            visited[row * cols + col] = True
            count = 1 + self.movingCountCore(threshold, rows, cols, row + 1, col, visited) \
                    + self.movingCountCore(threshold, rows, cols, row - 1, col, visited) \
                    + self.movingCountCore(threshold, rows, cols, row, col + 1, visited) \
                    + self.movingCountCore(threshold, rows, cols, row, col - 1, visited)
        return count

    def judgeCoord(self, threshold, row, col):
        if sum(map(int, str(row) + str(col))) <= threshold:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print s.movingCount(5, 10, 10)
