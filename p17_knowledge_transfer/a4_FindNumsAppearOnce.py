# -*- coding: UTF-8 -*-
"""
数组中只出现一次的数字。
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

解题思路：
方法一：用字典统计词频
方法二：位运算。遍历给定数组，对每个元素都进行异或运算，相同元素之间异或的结果为0，最终的异或结果为那两个只出现一次的数字之间的异或结果。
然后找到异或结果最右侧的1的位置，通过该位来区分那两个只出现一次的数字
"""


class Solution1:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        dic = {}
        for i in array:
            if str(i) in dic:
                dic[str(i)] += 1
            else:
                dic[str(i)] = 1
        result = []
        for k in dic.keys():
            if dic[k] == 1:
                result.append(int(k))
        return result


class Solution2:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        xor = 0
        for i in array:
            xor ^= i
        idxOf1 = self.getFirstIdxOf1(xor)
        num1, num2 = 0, 0
        for i in array:
            if (i >> idxOf1) & 1:
                num1 ^= i
            else:
                num2 ^= i
        return [num1, num2]

    def getFirstIdxOf1(self, num):
        idx = 0
        while num & 1 == 0 and idx < 32:
            idx += 1
            num = num >> 1
        return idx
