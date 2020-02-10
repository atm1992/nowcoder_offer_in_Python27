# -*- coding: UTF-8 -*-
"""
合并两个排序的链表。
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解题思路：使用递归或者循环
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    # 返回合并后列表。循环
    def Merge(self, pHead1, pHead2):
        # 避免pTemp.next报错，None没有next属性
        pMergeHead = ListNode(0)
        pTemp = pMergeHead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                pTemp.next = pHead1
                pHead1 = pHead1.next
            else:
                pTemp.next = pHead2
                pHead2 = pHead2.next
            pTemp = pTemp.next
        if pHead1:
            pTemp.next = pHead1
        if pHead2:
            pTemp.next = pHead2
        return pMergeHead.next


class Solution2:
    # 返回合并后列表。递归
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead
