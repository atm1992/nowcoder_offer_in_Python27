# -*- coding: UTF-8 -*-
"""
树的子结构。
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

解题思路：
首先，在A中查找与B根节点值相等的节点R; 使用递归遍历A
然后，判断A中以R为根节点的子树是否包含B，使用另一个方法进行递归
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            # 若在A中找到了B根节点值，则进入解题思路的第二步
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HasTree2(pRoot1, pRoot2)
            # 若A中当前节点值不等于B根节点值，或者第二步返回False，则继续递归在A中查找与B根节点值相等的节点R
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        # 递归终止条件
        # pRoot2为None，表示Tree2遍历完毕，可以返回
        if not pRoot2:
            return True
        # pRoot1为None，而此时的pRoot2不为None，因此返回False
        if not pRoot1:
            return False
        # 两节点的值不相等，返回False
        if pRoot1.val != pRoot2.val:
            return False
        # 递归遍历左子树和右子树
        return self.DoesTree1HasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right, pRoot2.right)
