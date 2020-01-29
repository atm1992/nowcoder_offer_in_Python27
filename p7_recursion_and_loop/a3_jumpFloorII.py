# -*- coding:utf-8 -*-
"""
变态跳台阶。
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
问题分析：
f(n) = f(n-1) + f(n-2) + …… + f(1) + f(0)
f(n-1) = f(n-2) + f(n-3) + …… + f(1) + f(0)
……
其中，f(n-1)表示第一步跳1级之后的步数，f(n-2)表示第一步跳2级之后的步数 ……
f(1)表示第一步跳n-1级之后的步数（只剩1级台阶了），因此 f(1) = 1
f(0)表示第一步跳n级之后的步数（剩余0级台阶了），因此 f(0) = 0
由上可知，f(n) = f(n-1) + (f(n-2) + …… + f(1) + f(0)) = f(n-1) + f(n-1) = 2*f(n-1)
"""


class Solution:
    def jumpFloorII_1(self, number):
        """方法一：使用递归"""
        if number == 0:
            return 0
        if number == 1:
            return 1
        return 2 * self.jumpFloorII_1(number - 1)

    def jumpFloorII_2(self, number):
        """方法二：使用for循环来代替递归"""
        if number == 0:
            return 0
        if number == 1:
            return 1
        # a保存倒数第一个子状态的数据
        a = 1
        ret = 0
        for _ in range(2, number + 1):
            ret = 2 * a
            a = ret
        return ret

    def jumpFloorII_3(self, number):
        """方法三：根据数学推导，直接返回结果。
        f(n) = 2*f(n-1) = 2*(2*f(n-2)) = …… = 2^i * f(n-i) = 2^(n-1) * f(n-(n-1))
        即 f(n) = 2^(n-1) * f(1) = 2^(n-1)
        """
        if number < 1:
            return 0
        # return pow(2, number - 1)
        return 2**(number - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII_3(10))
