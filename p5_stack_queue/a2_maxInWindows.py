#-*- coding: UTF-8 -*-
"""
滑动窗口的最大值。
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

解题思路：使用一个长度为size的临时数组来保存当前的最大值以及最多size-1个次大值的下标索引。其实临时数组的长度为 size-1 也是可以的
"""


class Solution:
    def maxInWindows(self, num, size):
        if not num or len(num) < size or size < 1:
            return []
        if size == 1:
            return num
        # 以下为size大于1，len(num)大于1
        # temp中的初始值为第一个元素的下标
        result, temp = [], [0]
        n = len(num)
        # 从1到n-1进行循环
        for i in range(1, n):
            # 判断当前temp数组中的第一个元素是否过期
            if i - temp[0] >= size:
                temp.pop(0)
            # 判断当前元素是否大于等于temp数组中的最后一个元素
            # 若符合条件，则pop掉最后一个元素，直到temp数组为空
            while temp and num[i] >= num[temp[-1]]:
                temp.pop()
            # 若temp的长度还没达到size，则将当前元素追加到temp数组中。当前元素小于此时的temp最后一个元素
            # 其实temp的长度为 size-1 也是可以的
            if len(temp) < size:
                temp.append(i)
            # 当前元素的下标达到size-1时，此后每次循环输出一个最大值。
            # 因为下标是从0开始
            if i >= size - 1:
                result.append(num[temp[0]])
        return result
