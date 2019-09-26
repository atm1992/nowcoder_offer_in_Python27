# -*- coding:utf-8 -*-
"""
二维数组中的查找。
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    # array 二维列表
    def Find_1(self, target, array):
        """方法一：常规扫描整个二维数组。时间复杂度为O(n*m) 行数*列数，可视为O(n^2)
        没有用到 每行从左到右递增、每列从上到下递增 的特性"""
        row_num = len(array)
        # 扫描行
        for i in range(row_num):
            col_num = len(array[i])
            # 扫描列
            for j in range(col_num):
                if array[i][j] == target:
                    return True
        return False

    def Find_2(self, target, array):
        """方法二：利用 每行从左到右递增、每列从上到下递增 的特性，减少扫描、比较次数。时间复杂度为O(n)"""
        row_num = 0
        col_num = len(array[0]) - 1
        row_count = len(array)
        while row_num < row_count and col_num >= 0:
            val = array[row_num][col_num]
            if val == target:
                return True
            elif val > target:
                col_num -= 1
            else:
                row_num += 1
        return False
