# -*- coding: UTF-8 -*-
from __future__ import print_function

"""
深度优先遍历 使用递归或栈
广度优先遍历 使用队列
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pre_in_build_tree(self, pre, tin):
        """使用前序序列和中序序列构建二叉树。要求所输入的前序序列和中序序列中不含重复数字，
        因为需要根据数值来确定根节点在中序序列中的位置"""
        if not pre or not tin:
            return None
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        # 构建左子树
        root.left = self.pre_in_build_tree(pre[1:i + 1], tin[:i])
        # 构建右子树
        root.right = self.pre_in_build_tree(pre[i + 1:], tin[i + 1:])
        return root

    def bfs_build_tree(self, bfs_li):
        """使用层次序列构建二叉树。所输入的层次序列任意，可以有None，可以重复"""
        if not bfs_li or len(bfs_li) < 1:
            return None
        root = TreeNode(bfs_li.pop(0))
        nodes = [root]
        while bfs_li:
            cur = nodes.pop(0)
            node = TreeNode(bfs_li.pop(0))
            cur.left = node
            nodes.append(node)
            if bfs_li:
                node = TreeNode(bfs_li.pop(0))
                cur.right = node
                nodes.append(node)
        return root

    def preorder(self, node):
        """深度优先遍历 之 先序遍历。根节点、左子树/节点、右子树/节点"""
        # 递归终止条件
        if not node:
            return None
        # 先打印传入节点（根节点）的信息
        print(node.val, end=" ")
        # 然后打印传入节点（根节点）的左子树上的所有节点的信息
        self.preorder(node.left)
        # 最后打印传入节点（根节点）的右子树上的所有节点的信息
        self.preorder(node.right)

    def preorder_non_recursive(self, node):
        """先序遍历的非递归版本"""
        if not node:
            return None
        stack = [node]
        while stack:
            cur_node = stack.pop()
            # 最先打印根节点
            print(cur_node.val, end=" ")
            # 右孩子节点先入栈，后出栈
            if cur_node.right:
                stack.append(cur_node.right)
            # 左孩子节点后入栈，先出栈
            if cur_node.left:
                stack.append(cur_node.left)

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

    def inorder_non_recursive(self, node):
        """中序遍历的非递归版本"""
        if not node:
            return None
        stack = []
        cur_node = node
        while cur_node or stack:
            if cur_node:
                # 先一路找到最左子节点
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                print(cur_node.val, end=" ")
                cur_node = cur_node.right

    def postorder(self, node):
        """深度优先遍历 之 后序遍历。左子树/节点、右子树/节点、根节点"""
        # 递归终止条件
        if not node:
            return None
        # 先打印传入节点（根节点）的左子树上的所有节点的信息
        self.postorder(node.left)
        # 然后打印传入节点（根节点）的右子树上的所有节点的信息
        self.postorder(node.right)
        # 最后打印传入节点（根节点）的信息
        print(node.val, end=" ")

    def postorder_non_recursive(self, node):
        """后序遍历的非递归版本。若类似于前序遍历直接写，会有些麻烦，因为这里需要判断节点的访问状态，根节点需要最后出栈。
        转换思路，将后序(左->右->根)看作是(根->右->左)的逆序"""
        if not node:
            return None
        stack = [node]
        res = []
        while stack:
            cur_node = stack.pop()
            # 先打印根节点
            res.append(cur_node.val)
            # 左孩子节点先入栈，后出栈
            if cur_node.left:
                stack.append(cur_node.left)
            # 右孩子节点后入栈，先出栈
            if cur_node.right:
                stack.append(cur_node.right)
        # res.reverse()
        # return res
        while res:
            print(res.pop(), end=" ")

    def breadth_travel(self, root):
        """广度优先遍历（即 层次遍历）"""
        if not root:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.val, end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


if __name__ == '__main__':
    s = Solution()
    # bfs_li = [8, 6, 6, 5, 7, 7, 5]
    bfs_li = [8, 7, 3, 9, 8, None, 5, 3, 3, None, 4]
    pre_li = [8, 7, 9, 3, 3, 8, None, 4, 3, None, 5]
    in_li = [3, 9, 3, 7, None, 8, 4, 8, None, 3, 5]
    post_li = [3, 3, 9, None, 4, 8, 7, None, 5, 3, 8]
    root = s.bfs_build_tree(bfs_li)
    # root = s.pre_in_build_tree(pre_li, in_li)
    print("层次序列：")
    s.breadth_travel(root)
    print("\n前序序列：")
    s.preorder(root)
    print("\n前序序列(非递归)：")
    s.preorder_non_recursive(root)
    print("\n中序序列：")
    s.inorder(root)
    print("\n中序序列(非递归)：")
    s.inorder_non_recursive(root)
    print("\n后序序列：")
    s.postorder(root)
    print("\n后序序列(非递归)：")
    s.postorder_non_recursive(root)
