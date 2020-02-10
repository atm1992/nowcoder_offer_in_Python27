# -*- coding: UTF-8 -*-
"""
二叉搜索树的后序遍历序列。
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

解题思路：后序遍历序列的最后一个元素是根节点，然后根据元素值的大小来切分左子树和右子树。然后使用递归
二叉搜索树 —— 对于树中的任意节点，其左边的所有子孙节点值都小于等于它，而右边的所有子孙节点值都大于等于它
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        n = len(sequence)
        root = sequence[-1]
        # split的初值必须为n-1。不能为0，也不能为n，考虑下只有左子树的情况，此时split的值不会被更新
        split = n - 1
        for i in range(n - 1):
            if sequence[i] > root:
                split = i
                break
        for i in range(split, n - 1):
            if sequence[i] < root:
                return False
        left, right = True, True
        # 确认左子树不为空。若为空，则不需要继续递归
        if split > 0:
            # 若split的初值为n，此时只有左子树（split的值不会被更新），sequence[:n]就是原始序列，然后递归会进入死循环
            left = self.VerifySquenceOfBST(sequence[:split])
        # 确认右子树不为空。若为空，则不需要继续递归
        if split < n - 1:
            # 若split的初值为0，此时只有左子树（split的值不会被更新），实际上的sequence[0:n-1]并不是右子树
            right = self.VerifySquenceOfBST(sequence[split:n - 1])
        return left and right
