# -*- coding: UTF-8 -*-
"""
数组中的逆序对。
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007。

题目保证输入的数组中没有相同的数字
数据范围：对于50%的数据,size<=10^4；对于75%的数据,size<=10^5；对于100%的数据,size<=2*10^5

例如：输入1,2,3,4,5,6,7,0    输出7         即 组成逆序对的两个数字并不一定是相邻的

解题思路：暴力破解法会运行超时。这里采用分治法。
使用归并排序的思路，先将原始数组一直对半切，直到子数组的长度小于2。然后一边合并子数组，一边统计逆序对的数量。统计逆序对的工作发生在子数组的合并过程。
"""


class Solution1:
    def InversePairs(self, data):
        """暴力破解。运行超时：5/6 组用例通过"""
        count = 0
        # 能用for循环就尽量不用while循环。for循环的执行效率更高；另外，for循环条件中的方法只会被调用 1 次，而while循环条件中的方法每次都会被调用。
        # sorted()会返回一个新数组，默认升序，并不会修改原始数组data
        for item in sorted(data):
            idx = 0
            if data[0] != item:
                idx = data.index(item)
                count += idx
            data.pop(idx)
        return count % 1000000007


class Solution2:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        """归并排序，分治法"""
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
        l_len, r_len = len(left_li), len(right_li)
        result = []
        while l < l_len and r < r_len:
            # 题目保证输入的数组中没有相同的数字
            if left_li[l] < right_li[r]:
                result.append(left_li[l])
                l += 1
            else:
                result.append(right_li[r])
                r += 1
                # 在归并排序的合并子数组过程中添加了一行统计逆序对
                # 若左侧的当前元素大于右侧的当前元素，则左侧该元素后面的所有元素都大于右侧的当前元素
                self.count += l_len - l
        return result + left_li[l:] + right_li[r:]
