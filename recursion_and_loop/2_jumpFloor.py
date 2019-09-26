# -*- coding:utf-8 -*-
"""
跳台阶。
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


class Solution:
    def jumpFloor_1(self, number):
        """方法一：递归实现。时间复杂度为O(2^n)
        跳n级台阶可分为两种情况：第一步跳1级（然后跳n-1级）、第一步跳2级（然后跳n-2级）
        f(n)=f(n-1)+f(n-2)
        """
        if number < 1:
            return 0
        if number == 1:
            # 跳一步1级
            return 1
        if number == 2:
            # 跳两步1级、跳一步2级
            return 2
        # 以下递归可处理number大于2的情况，边界条件为number小于等于2
        return self.jumpFloor_1(number - 1) + self.jumpFloor_1(number - 2)

    def jumpFloor_2(self, number):
        """方法二：使用for循环来代替递归。时间复杂度为O(n)"""
        if number < 1:
            return 0
        if number == 1:
            # 跳一步1级
            return 1
        if number == 2:
            # 跳两步1级、跳一步2级
            return 2
        # a保存倒数第二个子状态的数据，b保存倒数第一个子状态的数据，ret保存当前状态的数据
        a, b = 1, 2
        ret = 0
        # number小于3时，不会进入循环，也并不会报错
        for _ in range(3, number + 1):
            ret = a + b
            a, b = b, ret
        return ret

    def jumpFloor_3(self, number):
        """方法三：使用一个列表来保存从0到number的所有结果。时间复杂度为O(n)，空间复杂度也为O(n)
        适用于需要多次获取结果的情况"""
        # 初始列表保存着number为0、1、2时的结果
        res = [0, 1, 2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor_3(10))
