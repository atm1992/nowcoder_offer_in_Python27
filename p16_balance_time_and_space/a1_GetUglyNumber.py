# -*- coding:utf-8 -*-
"""
丑数。
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
解题思路：
对于任意一个丑数（1除外），一定等于一个较小的丑数乘以2、3或5得到
问题的关键在于如何确保这些丑数有序，即保证 一个丑数乘以2、另一个较小的丑数乘以3、另一个更小的丑数乘以5 这三个丑数之间的顺序
可以设定3个指针变量分别指向需要乘以2、3或5的那个丑数，这3个指针变量都是从小到大的遍历所有丑数
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        # 初始化一个数组用来存放有序的丑数，初始值均为1，长度为index
        ugly_number = [1] * index
        # index2表示需要乘以2的那个丑数的下标。刚开始index2、index3、index5都指向第一个丑数
        index2 = 0
        index3 = 0
        index5 = 0
        # cur_index指向当前待插入丑数的位置
        cur_index = 1
        while cur_index < index:
            # 避免反复从数组中获取元素值
            ugly2, ugly3, ugly5 = ugly_number[index2] * 2, ugly_number[index3] * 3, ugly_number[index5] * 5
            min_value = min(ugly2, ugly3, ugly5)
            ugly_number[cur_index] = min_value
            # 使用3个if，而不是if……elif……else，是因为可能存在ugly2、ugly3、ugly5中的两个或三个同时都等于min_value的情况，
            # 从而避免在之后插入重复的丑数
            if ugly2 == min_value:
                index2 += 1
            if ugly3 == min_value:
                index3 += 1
            if ugly5 == min_value:
                index5 += 1
            cur_index += 1
        return ugly_number[index - 1]
