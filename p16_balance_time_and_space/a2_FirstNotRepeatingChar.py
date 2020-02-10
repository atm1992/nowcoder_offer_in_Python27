# -*- coding: UTF-8 -*-
"""
第一个只出现一次的字符。
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）。

解题思路：使用字典来统计每个字符的出现次数
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        store = {}
        li = list(s)
        for i in li:
            if i in store.keys():
                store[i] += 1
            else:
                store[i] = 1
        for i in li:
            if store[i] == 1:
                return li.index(i)
        return -1
