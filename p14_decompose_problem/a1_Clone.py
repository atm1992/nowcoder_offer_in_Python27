# -*- coding: UTF-8 -*-
"""
复杂链表的复制。
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

解题思路：分治法。将原始链表看作一长串节点，pHead是原始链表的第一个节点。
一、在每个原始节点的后面插入当前节点的复制节点
二、对各个复制节点的random链接进行赋值
三、拆分链表。奇数位置的所有节点组成原始链表，偶数位置的所有节点组成复制链表。返回复制链表的头结点即可
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        pNode = pHead
        # 在每个原始节点的后面插入当前节点的复制节点
        while pNode:
            pClone = RandomListNode(pNode.label)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next
        pNode = pHead
        # 对各个复制节点的random链接进行赋值
        while pNode:
            pClone = pNode.next
            if pNode.random:
                pClone.random = pNode.random.next
            pNode = pClone.next
        pNode = pHead
        # 拆分链表
        pCloneHead = pClone = pNode.next
        pNode.next = pClone.next
        pNode = pNode.next
        while pNode:
            pClone.next = pNode.next
            pClone = pClone.next
            pNode.next = pClone.next
            pNode = pNode.next
        return pCloneHead
