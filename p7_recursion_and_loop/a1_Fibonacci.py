# -*- coding:utf-8 -*-
"""
斐波那契数列。
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
f(0)=0  f(1)=1
f(2)=1  f(3)=2
f(4)=3  f(5)=5
"""


class Solution:
    def Fibonacci_1(self, n):
        """方法一：递归实现。时间复杂度为O(2^n)"""
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci_1(n - 1) + self.Fibonacci_1(n - 2)

    def Fibonacci_2(self, n):
        """方法二：使用for循环来代替递归。时间复杂度为O(n)"""
        if n == 0:
            return 0
        if n == 1:
            return 1
        # a保存倒数第二个子状态的数据，b保存倒数第一个子状态的数据，ret保存当前状态的数据
        a, b = 0, 1
        ret = 0
        for _ in range(2, n + 1):
            ret = a + b
            a, b = b, ret
        return ret

    def Fibonacci_3(self, n):
        """方法三：使用一个列表来保存从0到n的斐波那契数。时间复杂度为O(n)，空间复杂度也为O(n)
        适用于需要多次获取斐波那契数的情况
        """
        # 初始列表保存着n为0、1时的结果
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]

    def Fibonacci_4(self, n):
        """使用一个列表来保存前两个斐波那契数。时间复杂度为O(n)"""
        # 初始列表保存着n为0、1时的结果
        res = [0, 1]
        for i in range(2, n + 1):
            res[i % 2] = res[0] + res[1]
        return res[n % 2]


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci_4(100))
