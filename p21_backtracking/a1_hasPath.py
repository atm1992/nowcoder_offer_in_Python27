# -*- coding: UTF-8 -*-
"""
矩阵中的路径。
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如：a b c e s f c s a d e e 这样的 3x4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

解题思路：回溯法。首先遍历字符矩阵(一维数组)，找到path中的第一个字符，然后遍历该字符的上下左右4个字符，若存在与path中下一个字符相同的字符，
则将其作为下一次遍历的起点，否则回退到上一个字符，重新遍历。为避免重复进入已遍历格子，需要使用一个与原字符矩阵相同大小的辅助矩阵(也是一个一维数组)
来记录原字符矩阵中对应位置的字符是否已在当前的遍历路径中
"""


class Solution:
    # matrix —— 字符矩阵；rows —— 矩阵的行数；cols —— 矩阵的列数；path —— 待查找路径(字符串)
    # 注意：输入的字符矩阵matrix存储在一个一维数组中
    def hasPath(self, matrix, rows, cols, path):
        # 参数校验
        if not matrix or rows < 1 or cols < 1 or len(matrix) != rows * cols or not path:
            return False
        # 辅助矩阵，记录原矩阵各个位置的字符是否已在当前的遍历路径中
        visited = [False] * (rows * cols)
        # 当前已遍历路径的长度，当该值等于待查找路径path的长度时，说明路径存在，遍历结束
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                # 这里的双重循环只是为了给定一个起始点，待查找路径中的其它字符在下面的递归中找到
                # 若下面的递归跑了一圈没找到，则重新更换一个起始点继续。当下面这个函数返回True时，说明已找到完整路径
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if pathLength == len(path):
            return True
        curHasPath = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[pathLength] and not visited[row * cols + col]:
            pathLength += 1
            visited[row * cols + col] = True
            curHasPath = self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited) \
                         or self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) \
                         or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) \
                         or self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited)
            if not curHasPath:
                pathLength -= 1
                visited[row * cols + col] = False
        return curHasPath
