# -*- coding:utf-8 -*-
"""
从尾到头打印链表。
输入一个链表，按链表从尾到头的顺序返回一个ArrayList
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """从头到尾读取链表数据，然后利用头插法将数据插入到返回的结果序列"""
        ret = []
        while listNode:
            ret.insert(0, listNode.val)
            listNode = listNode.next
        return ret
