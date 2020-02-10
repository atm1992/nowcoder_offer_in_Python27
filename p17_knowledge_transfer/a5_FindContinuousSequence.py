# -*- coding: UTF-8 -*-
"""
和为S的连续正数序列。
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

解题思路：举例说明
以和为9为例，令small为1、big为2，此时的连续序列为[1,2]，和为3，小于9；因此big+1变为3，此时的连续序列为[1,2,3]，和为6，依然小于9；
因此big再加1，此时的连续序列为[1,2,3,4]，和为10，大于9；此时则需要从连续序列中删除一些数字，从最小的small开始，即连续序列变为
[2,3,4]，此时的和为9，满足条件，将该序列添加到结果数组中。然后再增加big、删除small……，接着便可找到第二个连续序列[4,5]
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # 因为要求序列长度至少为2，并且是正数，即最小必须为3 = 1+2
        if not tsum or tsum < 3:
            return []
        small, big = 1, 2
        cur_sum = small + big
        result = []
        # 因为要求序列长度至少为2，所以连续序列的最小值small必须小于最大值big
        while small < big:
            if cur_sum > tsum:
                cur_sum -= small
                small += 1
            else:
                if cur_sum == tsum:
                    result.append([i for i in range(small, big + 1)])
                big += 1
                cur_sum += big
        return result
