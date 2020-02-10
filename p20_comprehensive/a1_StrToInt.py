# -*- coding: UTF-8 -*-
"""
把字符串转换成整数。
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入：输入一个字符串,包括数字字母符号,可以为空
输出：如果是合法的数值表达则返回该数字，否则返回0
例如：+2147483647 ——> 2147483647；1a33 ——> 0

解题思路：int为32位，需要判断是否溢出
"""


class Solution:
    def StrToInt(self, s):
        # '0'后面无论接什么，返回结果都是0
        if not s or s[0] == '0':
            return 0
        flag, result = 1, 0
        numdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if s[0] in '+-':
            if len(s) == 1 or s[1] == '0':
                return 0
            if s[0] == '-':
                flag = -1
            s = s[1:]
        for i in s:
            if i not in numdict.keys():
                return 0
            else:
                result = result * 10 + numdict[i]
        result *= flag
        # ~0x7fffffff 等于 -0x80000000
        return result if -0x80000000 <= result <= 0x7fffffff else 0
