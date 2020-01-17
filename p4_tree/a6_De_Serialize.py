#-*- coding: UTF-8 -*-
from __future__ import print_function
"""
序列化二叉树。
请实现两个函数，分别用来序列化和反序列化二叉树。

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

解题思路：不适合使用层次遍历，因为在序列化的时候，无法保存序列中间的空节点。这里采用的是前序遍历，反序列化其实就是重建一棵树，
之所以可以只使用前序序列重建，是因为这里的前序序列使用#保留了空节点的位置。通常的前序、中序、后序都不保留空节点的位置。
以"2,#,#"为例，表示2的左右孩子均为空节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        pre_li = s.split(',')
        return self.deserializeTree(pre_li)

    def deserializeTree(self, pre_li):
        if len(pre_li) < 1:
            return None
        val = pre_li.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            # 当root的左孩子为空时，才会执行下一句的右孩子
            root.left = self.deserializeTree(pre_li)
            root.right = self.deserializeTree(pre_li)
        return root

    def inorder(self, node):
        """深度优先遍历 之 中序遍历。左子树/节点、根节点、右子树/节点"""
        # 递归终止条件
        if not node:
            return None
        # 先打印传入节点（根节点）的左子树上的所有节点的信息
        self.inorder(node.left)
        # 然后打印传入节点（根节点）的信息
        print(node.val, end=" ")
        # 最后打印传入节点（根节点）的右子树上的所有节点的信息
        self.inorder(node.right)


if __name__ == '__main__':
    s = Solution()
    li = [5, 4, "#", 3, "#", 2]
    li_s = ",".join(map(str, li))
    root = s.Deserialize(li_s)
    print("中序遍历：")
    print(s.inorder(root))
    print("前序遍历：")
    print(s.Serialize(root))
