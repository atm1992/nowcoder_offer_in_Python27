# -*- coding: UTF-8 -*-
"""
把数组排成最小的数。
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

解题思路：可看作一个排序问题。对于两个字符串数字s1、s2，若s1拼接s2得到的数字大于s2拼接s1得到的数字，则s2应该放在s1的前面
"""


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        str_nums = [str(n) for n in numbers]
        n = len(str_nums)
        # 对str_nums进行排序
        for i in range(n - 1):
            for j in range(i + 1, n):
                if str_nums[i] + str_nums[j] > str_nums[j] + str_nums[i]:
                    str_nums[i], str_nums[j] = str_nums[j], str_nums[i]
        return ''.join(str_nums)
