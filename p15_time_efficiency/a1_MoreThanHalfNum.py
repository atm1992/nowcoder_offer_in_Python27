# -*- coding: UTF-8 -*-
"""
数组中出现次数超过一半的数字。
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

解题思路：
方法一：使用一个dict统计数组中各个数字的出现次数，在统计过程中，判断当前数字的出现次数是否超过一半，若遍历完整个数组也没找到，则返回0

方法二：使用count来统计一个元素的出现次数，若当前遍历到的元素等于被统计元素，则count加1，否则减1。
若count减为0，则将被统计元素换成当前元素，并将count置为1。遍历完数组后，再统计result的出现次数，判断是否超过一半

本题更倾向于使用方法一。方法二的适用场景：数组中一定存在出现次数超过一半的数字（此时可以直接返回结果，而无需再判断出现次数是否超过一半）
"""


class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        n = len(numbers)
        if n == 1:
            return numbers[0]
        wc = {}
        for i in range(n):
            if numbers[i] in wc:
                wc[numbers[i]] += 1
                if wc[numbers[i]] > n // 2:
                    return numbers[i]
            else:
                wc[numbers[i]] = 1
        return 0


class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        n = len(numbers)
        if n == 1:
            return numbers[0]
        result = numbers[0]
        count = 1
        for i in range(1, n):
            if count == 0:
                result = numbers[i]
                count = 1
            elif numbers[i] == result:
                count += 1
            else:
                count -= 1
        if self.isMoreThanHalf(numbers, n, result):
            return result
        return 0

    def isMoreThanHalf(self, numbers, length, number):
        count = 0
        for i in range(length):
            if numbers[i] == number:
                count += 1
        if count > length // 2:
            return True
        return False
