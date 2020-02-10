# -*- coding: UTF-8 -*-
"""
包含min函数的栈。
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

解题思路：使用两个stack，一个为数据栈，另一个为辅助栈。数据栈用于存储所有数据；辅助栈用于存储最小值。
两个栈的元素个数相同，同时append元素以及同时pop元素，区别就是辅助栈每次都是append当前的最小元素。
这样做是避免数据栈已经将最小值pop掉了，而辅助栈中还保留着

可以使用Python数组来实现栈，Python数组的append、pop操作都是在数组的末尾进行，因此可把数组的末尾当做栈顶。
注意：执行pop操作时，数组不能为空
"""


class Solution1:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if not self.minStack or node < self.min():
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())

    def pop(self):
        # 因为stack与minStack的长度相等，因此只需验证stack不为空即可
        if self.stack:
            self.minStack.pop()
            self.stack.pop()
        else:
            return None

    # 这里是获取栈顶元素。虽然pop也可获得栈顶元素，但是若使用pop，栈顶元素将会被弹出，之后便获取不到了。
    # 因此不能使用pop来代替top
    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]


class Solution2:
    # 减小辅助栈的长度，只有满足一定条件才append、pop辅助栈
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        # 当前元素小于或等于当前最小值时append，只保留当前的最小值及其重复值
        if not self.minStack or node <= self.min():
            self.minStack.append(node)

    def pop(self):
        if not self.stack:
            return None
        if self.top() == self.min():
            self.minStack.pop()
        self.stack.pop()

    # 这里是获取栈顶元素。虽然pop也可获得栈顶元素，但是若使用pop，栈顶元素将会被弹出，之后便获取不到了。
    # 因此不能使用pop来代替top
    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]
