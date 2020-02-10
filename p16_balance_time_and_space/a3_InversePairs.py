# -*- coding: UTF-8 -*-
"""
数组中的逆序对。
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007。

题目保证输入的数组中没有的相同的数字
数据范围：对于50%的数据,size<=10^4；对于75%的数据,size<=10^5；对于100%的数据,size<=2*10^5

例如：输入1,2,3,4,5,6,7,0    输出7         即 组成逆序对的两个数字并不一定是相邻的

解题思路：暴力法会运行超时。这里采用分治法。
使用归并排序的思路，先将原始数组一直对半切，直到子数组的长度小于2。然后一边合并子数组，一边统计逆序对的数量。统计逆序对的工作发生在子数组的合并过程。

注意：这道题若使用Python，将会运行超时，已放弃！
"""


class Solution1:
    # 运行超时。case通过率为50.00%
    def InversePairs(self, data):
        count = 0
        # sorted()会返回一个新数组，而并不会修改原始数组data
        for item in sorted(data):
            count += data.index(item)
            data.remove(item)
        return count % 1000000007


class Solution2:
    # 归并排序，分治法。case通过率为75.00%，使用其它语言(Java、C++)可以完全通过，Python只能最多75%，放弃了
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        if not data or len(data) < 2:
            return 0
        self.merge_sort(data)
        return self.count % 1000000007

    def merge_sort(self, li):
        n = len(li)
        if n < 2:
            return li
        mid = n // 2
        left_li = self.merge_sort(li[:mid])
        right_li = self.merge_sort(li[mid:])
        l, r = 0, 0
        result = []
        while l < len(left_li) and r < len(right_li):
            # 题目保证输入的数组中没有的相同的数字
            if left_li[l] <= right_li[r]:
                result.append(left_li[l])
                l += 1
            else:
                result.append(right_li[r])
                r += 1
                # 在归并排序的合并子数组过程中添加了一行统计逆序对
                # 若左侧的当前元素大于右侧的当前元素，则左侧该元素后面的所有元素都大于右侧的当前元素
                self.count += len(left_li) - l
        return result + left_li[l:] + right_li[r:]

