# -*- coding: UTF-8 -*-
"""
最小的K个数。
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

解题思路：若数据量较小且数据不变，则可先完全排序，然后取前k个；若数据量很大或者是流数据，则可使用大小为K的最大堆。
方法一：快速排序。不稳定排序，该方法会修改原始数组
方法二：堆排序。维护一个大小为K的最大堆，注意是最大堆，而不是最小堆。遍历原始数组时，若当前元素小于堆顶元素，则将堆顶元素替换为当前元素，并调整最大堆

注意：二叉堆虽然是一颗完全二叉树，但二叉堆并不是使用链式存储，而是采用的顺序存储，即 二叉堆的所有节点都存储在数组当中。
因为没有左右指针，因此二叉堆通过计算数组下标来定位左右孩子，数组下标从0开始，即 根节点的下标为0
"""


class Solution:
    # 先对原始数组进行快速排序，然后返回排序结果中的前K位
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput) or k <= 0:
            return []
        tinput = self.quick_sort(tinput)
        return tinput[:k]

    def quick_sort(self, lst):
        if len(lst) < 2:
            return lst
        mid = lst[0]
        left = self.quick_sort([x for x in lst[1:] if x <= mid])
        right = self.quick_sort([x for x in lst[1:] if x > mid])
        return left + [mid] + right
