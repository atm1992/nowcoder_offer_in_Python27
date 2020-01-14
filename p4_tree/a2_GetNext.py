# -*- coding: UTF-8 -*-

"""
二叉树的下一个节点。
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

解题思路：
中序遍历（左根右），将给定节点视为某子树的根节点（叶节点可视为空子树的根节点），因此下一个节点是右
1、若给定节点的右子树不为空，则向下查找，找到右子树中的最左节点
2、若给定节点的右子树为空，说明当前子树遍历完毕，则向上查找，找到某个根节点（该节点的左子树是包含给定节点的最小子树）
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                else:
                    pNode = pNode.next
            return None
