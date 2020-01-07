# -*- coding:utf-8 -*-
"""
链表中倒数第k个结点。
输入一个链表，输出该链表中倒数第k个结点。
借助两个临时指针变量p1、p2，p1先走到第k个位置
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k < 1:
            return None
        p1 = head
        p2 = None
        # p1向后移动k-1次，移动到第k个位置
        for _ in range(k - 1):
            if p1.next:
                p1 = p1.next
            else:
                # 链表长度小于k
                return None
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2
