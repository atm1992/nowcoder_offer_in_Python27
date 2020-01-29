# -*- coding:utf-8 -*-
"""
矩形覆盖。
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
这个问题和跳台阶、斐波那契数列的本质是一样的。
刚开始第一步可分为两种情况：
1、用一个2*1的小矩形进行填充，剩余面积为2*(n-1)
2、用一个1*2的小矩形进行填充，剩余面积为2*(n-2) + 1*2，后面的那个1*2只能用1*2的小矩形填充
因此可知，f(n) = f(n-1)+f(n-2)
当n为0时，无需填充，f(0) = 0
当n为1时，只能使用一个2*1的小矩形进行填充，f(1) = 1
当n为2时，可使用两个2*1 或 两个1*2 进行填充，f(2) = 2
"""


class Solution:
    def rectCover_1(self, number):
        """方法一：使用一个列表只保存最近两个状态的结果。时间复杂度为O(n)，空间复杂度为O(1)"""
        if number < 1:
            return 0
        # 初始列表保存着number为1、2时的结果。number为奇数，放在res[0]；number为偶数，放在res[1]
        res = [1, 2]
        for i in range(3, number + 1):
            res[(i+1) % 2] = res[0] + res[1]
        return res[(number+1) % 2]

    def rectCover_2(self, number):
        """方法二：使用一个列表来保存从0到number的所有结果。时间复杂度为O(n)，空间复杂度也为O(n)
        适用于需要多次获取结果的情况"""
        # 初始列表保存着number为0、1、2时的结果
        res = [0, 1, 2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]
