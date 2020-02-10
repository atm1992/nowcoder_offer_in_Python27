# -*- coding: UTF-8 -*-
"""
顺时针打印矩阵。
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
例如，如果输入如下4 x 4矩阵：
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

解题思路：可分解为从外到内顺时针一圈一圈打印，一圈又可分解为：从左到右横行、从上到下竖行、从右到左横行、从下到上竖行
终止条件为：1、只有一横行，只需从左到右即可；2、只有一竖列，从左到右、从上到下；3、只有两横行，从左到右、从上到下、从右到左；
4、只有两竖列，从左到右、从上到下、从右到左、从下到上
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        # 这个循环条件可通过画图来理解
        while rows > start * 2 and cols > start * 2:
            self.printMatrixInCircle(matrix, cols, rows, start, result)
            start += 1
        return result

    def printMatrixInCircle(self, matrix, cols, rows, start, result):
        # 所输入的matrix就是原始矩阵，start是当前圈起始点的行号和列号（行列号相等）
        # 剩余矩阵的最后一列在原始矩阵中的列号
        endX = cols - 1 - start
        # 剩余矩阵的最后一行在原始矩阵中的行号
        endY = rows - 1 - start
        # 从左到右打印横行
        for i in range(start, endX + 1):
            result.append(matrix[start][i])
        # 从上到下打印竖行
        for i in range(start + 1, endY + 1):
            result.append(matrix[i][endX])
        if start != endY:
            # 从右到左打印横行，剩余矩阵至少两行才需要
            for i in range(endX - 1, start - 1, -1):
                result.append(matrix[endY][i])
        if start != endX:
            # 从下到上打印竖行，剩余矩阵至少两列才需要
            for i in range(endY - 1, start, -1):
                result.append(matrix[i][start])
