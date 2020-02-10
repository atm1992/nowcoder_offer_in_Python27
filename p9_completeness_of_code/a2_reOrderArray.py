# -*- coding: UTF-8 -*-
"""
调整数组顺序使奇数位于偶数前面。
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

解题思路：
"""


class Solution1:
    def reOrderArray(self, array):
        # 重新定义待排序元素为0(偶数)或1(奇数)，reverse = True 降序，1(奇数)在前，0(偶数)在后
        # sorted是一个稳定排序，可以确保相同元素的相对位置
        return sorted(array, key=lambda a: a % 2, reverse=True)


class Solution2:
    def reOrderArray(self, array):
        if not array or len(array) < 1:
            return []
        n = len(array)
        first_even = 0
        # 找到第一个偶数所在的位置
        while first_even < n and array[first_even] & 1 == 1:
            first_even += 1
        odd = first_even + 1
        while odd < n:
            if array[odd] & 1 == 1:
                array.insert(first_even, array.pop(odd))
                first_even += 1
            odd += 1
        return array
