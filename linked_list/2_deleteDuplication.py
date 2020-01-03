# -*- coding:utf-8 -*-

"""
删除链表中重复的结点。
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
注意：链表是已排好序的，所以重复结点的位置肯定是相邻的
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        """借助两个临时指针变量，first固定为头结点的前一个结点，pre为待删除结点pHead的前一个结点
        first之所以不是指向头结点，是因为头结点也可能重复，需要被删除"""
        # 若链表为空或只有一个结点，则肯定不存在重复
        if pHead is None or pHead.next is None:
            return pHead
        # first结点的val可为任意值
        first = ListNode(-1)
        first.next = pHead
        pre = first
        # pHead为重复结点中的第一个结点，一个结点要存在重复，它的next结点必不为None
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                # 通过while循环删除重复结点
                while pHead and pHead.val == val:
                    pHead = pHead.next
                # 退出上句while循环时，pHead要么为None（到了末尾），要么pHead.val不再等于重复值
                pre.next = pHead
            else:
                # 此时pHead的值不等于pHead.next的值，说明pHead不重复
                pre = pHead
                pHead = pHead.next
        return first.next