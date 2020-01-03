# -*- coding:utf-8 -*-
"""
两个链表的第一个公共结点。
输入两个链表，找出它们的第一个公共结点。
注意：公共结点并不仅是两个结点的值相等，而是两个结点的值和指针域都相等，也就是说这两个结点其实就是同一个结点
由于这“两个”结点（其实是一个结点）的指针域相同，所以它们的后继结点也肯定是一样的，也就是说从第一个公共结点开始，这两个链表完全一样了
两个链表不一定等长，但链表尾部的公共部分长度肯定一样
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 若链表1或链表2为空，则返回None
        if pHead1 is None or pHead2 is None:
            return None
        # 定义两个临时指针变量
        p1, p2 = pHead1, pHead2
        len1, len2 = 0, 0
        # 获取链表的实际长度
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        # 若链表1比链表2长，则将链表1的pHead移动到与链表2等长的位置
        if len1 > len2:
            while len1 - len2 > 0:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            # 若链表2比链表1长，则将链表2的pHead移动到与链表1等长的位置
            while len2 - len1 > 0:
                pHead2 = pHead2.next
                len2 -= 1
        # 同时移动链表1和2的pHead，若pHead1和pHead2相等（指向了同一个结点），则返回该指针变量
        while pHead1 and pHead2:
            if pHead1 == pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None
