# -*- coding: UTF-8 -*-
"""
数值的整数次方。
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0

解题思路：因为指数exponent是整数，因此可以使用递归将指数每次都对半切，直到指数为0或1，这样可以减小计算量
"""


class Solution1:
    def Power(self, base, exponent):
        return base ** exponent


class Solution2:
    def Power(self, base, exponent):
        try:
            ret = self.power_value(base, abs(exponent))
            if exponent < 0:
                ret = 1.0 / ret
        except ZeroDivisionError:
            # 指数为负数时，底数不能为0.因为负指数相当于正指数的倒数，倒数的分母不能为0
            print("Error: base is zero")
        else:
            return ret

    def power_value(self, base, exponent):
        # 递归终止条件
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        # exponent//2 也可写成 exponent>>1
        ret = self.power_value(base, exponent // 2)
        ret *= ret
        # 判断指数是奇数还是偶数
        if exponent % 2 == 1:
            ret *= base
        return ret
